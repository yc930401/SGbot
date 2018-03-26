import random
import numpy as np
import dialog_config
import db_helper



class user_simulator():

    # init file path and load data
    def __init__(self):
        self.path_events_db = 'events_db.json'
        self.information_slot_names = dialog_config.INFORMATION_SLOTS
        self.request_slot_names = dialog_config.REQUEST_SLOTS
        self.event_data = self.__load_event_Data__()
        self.start_conversation()


    # init user goal and state
    def start_conversation(self):
        self.state = {}
        self.state['history_slots'] = {}
        self.state['inform_slots'] = {}
        self.state['request_slots'] = []
        self.state['rest_slots'] = []
        self.state['turn'] = 1
        self.state['act'] = dialog_config.DIALOG_ACT['INFORM']

        self.goal = {}
        self.goal['inform_slots'] = {}
        self.goal['request_slots'] = []

        self.dialog_status = dialog_config.DIALOG_STATUS['NO_OUTCOME_YET']

        self.agent_proposed = 0
        self.deny_count = 0


    # load event data which is used for generating user goal and state
    def __load_event_Data__(self):
        return db_helper.get_training_data()


    # first round: generate user agenda (user goal and initial state)
    def generate_user_agenda(self, max_turn):
        self.max_turn = max_turn
        self.start_conversation()
        data = self.event_data[np.random.randint(len(self.event_data))]
        all_slots = list(data.keys())
        # random select several slots
        number_of_slots = np.random.randint(6,8)
        random_choose_slots = [all_slots[i] for i in random.sample(range(len(all_slots)), number_of_slots)]
        random_inform_slots = int(number_of_slots/2)
        for slot in random_choose_slots:
            if slot in self.information_slot_names and slot != 'event' and \
                    len(self.goal['inform_slots']) < random_inform_slots:
                self.goal['inform_slots'][slot] = data[slot]
                if len(self.state['inform_slots']) < np.random.randint(1,3):
                    self.state['inform_slots'][slot] = data[slot]
                else:
                    self.state['rest_slots'].append(slot)
            elif slot in self.request_slot_names:
                self.goal['request_slots'].append(slot)
                self.state['rest_slots'].append(slot)

        self.state['request_slots'].append('event')
        print('User Goal: {}\nUser State: {}'.format(self.goal, self.state))

        sample_action = {}
        sample_action['act'] = self.state['act']
        sample_action['inform_slots'] = self.state['inform_slots']
        sample_action['request_slots'] = self.state['request_slots']
        sample_action['turn'] = self.state['turn']
        sample_action['sentence'] = ''

        return sample_action, self.dialog_status


    # user respond after the first round
    def generate_user_response(self, system_action):
        self.state['turn'] += 1
        self.dialog_status = dialog_config.DIALOG_STATUS['NO_OUTCOME_YET']

        sys_act = system_action['act']

        if (self.max_turn > 0 and self.state['turn'] > self.max_turn):
            self.state['act'] = dialog_config.DIALOG_ACT['CLOSING']
            self.dialog_status = dialog_config.DIALOG_STATUS['FAILED_DIALOG']
        else:
            self.state['history_slots'].update(self.state['inform_slots'])
            self.state['inform_slots'].clear()

            if sys_act == dialog_config.DIALOG_ACT['INFORM']:
                self.response_inform(system_action)
            elif sys_act == dialog_config.DIALOG_ACT['REQUEST']:
                self.response_request(system_action)
            elif sys_act == dialog_config.DIALOG_ACT['CONFIRM_ANSWER']:
                self.response_confirm_answer(system_action)
            elif sys_act == dialog_config.DIALOG_ACT['CLOSING']:
                self.response_closing(system_action)
            elif sys_act == dialog_config.DIALOG_ACT['GREETING']:
                self.response_greeting(system_action)

            if self.agent_proposed < self.deny_count:
               if system_action['act'] != dialog_config.DIALOG_ACT['INFORM']:
                   self.dialog_status = dialog_config.DIALOG_STATUS['FAILED_DIALOG']
                   self.state['act'] = dialog_config.DIALOG_ACT['CLOSING']
                   self.state['inform_slots'].clear()
                   self.state['request_slots'] = []
               elif 'event' not in system_action['inform_slots'].keys():
                   self.dialog_status = dialog_config.DIALOG_STATUS['FAILED_DIALOG']
                   self.state['act'] = dialog_config.DIALOG_ACT['CLOSING']
                   self.state['inform_slots'].clear()
                   self.state['request_slots'] = []
            if self.agent_proposed > self.deny_count+1:
                self.dialog_status = dialog_config.DIALOG_STATUS['FAILED_DIALOG']
                self.state['act'] = dialog_config.DIALOG_ACT['CLOSING']
                self.state['inform_slots'].clear()
                self.state['request_slots'] = []

        response_action = {}
        response_action['act'] = self.state['act']
        response_action['inform_slots'] = self.state['inform_slots']
        response_action['request_slots'] = self.state['request_slots']
        response_action['turn'] = self.state['turn']
        response_action['sentence'] = ''

        return response_action, self.dialog_status, self.state


    def response_inform(self, system_action):
        ''' Get temporary success or fail - return the correct(wrong) answer for user request slot '''
        self.dialog_status = dialog_config.DIALOG_STATUS['SUCCESS_TEMP']
        # Fail to find an event
        if 'event' in system_action['inform_slots'].keys():
            self.agent_proposed += 1
            if system_action['inform_slots']['event'] == dialog_config.SPECIAL_SLOT_VALUES['NO_VALUE_MATCH']:
                self.dialog_status = dialog_config.DIALOG_STATUS['SUCCESS_DIALOG']
                self.state['act'] = dialog_config.DIALOG_ACT['CLOSING']
                return
            else:
                rest_inform = list(set(self.state['rest_slots']) & set(self.goal['inform_slots']))
                if np.random.rand() <= (4 - len(self.state['history_slots']))*0.3:#min(1, len(rest_inform)*0.5): # deny
                    self.dialog_status = dialog_config.DIALOG_STATUS['FAILED_TEMP']
                    self.state['act'] = dialog_config.DIALOG_ACT['DENY']
                    if len(rest_inform) > 0:
                        selected_slot = random.choice(rest_inform)
                        self.state['inform_slots'][selected_slot] = self.goal['inform_slots'][selected_slot]
                        self.state['rest_slots'].remove(selected_slot)
                    self.deny_count += 1
                    return
                else:
                    rest_inform = list(set(self.state['rest_slots']) & set(self.goal['inform_slots']))
                    for inform in rest_inform:
                        self.state['rest_slots'].remove(inform)
                    # Ask new a question
                    rest_request = list(set(self.state['rest_slots']) & set(self.goal['request_slots']))
                    if len(rest_request) > 0:
                        selected_slot = random.choice(rest_request)
                        self.state['act'] = dialog_config.DIALOG_ACT['REQUEST']
                        self.state['request_slots'] = [selected_slot]
                        self.state['rest_slots'].remove(selected_slot)
                        return
                    else:
                        self.state['request_slots'] = []
                        self.state['act'] = dialog_config.DIALOG_ACT['CLOSING']
                        self.dialog_status = dialog_config.DIALOG_STATUS['SUCCESS_DIALOG']
                        return

        if len(self.state['request_slots']) > 0 :
            if self.state['request_slots'][0] in system_action['inform_slots'].keys():
                self.dialog_status = dialog_config.DIALOG_STATUS['SUCCESS_TEMP']
                # Ask new a question
                rest_request = list(set(self.state['rest_slots']) & set(self.goal['request_slots']))
                if len(rest_request) > 0:
                    selected_slot = random.choice(rest_request)
                    self.state['act'] = dialog_config.DIALOG_ACT['REQUEST']
                    self.state['request_slots'] = [selected_slot]
                    self.state['rest_slots'].remove(selected_slot)
                else:
                    self.state['request_slots'] = []
                    self.state['act'] = dialog_config.DIALOG_ACT['CLOSING']
                    self.dialog_status = dialog_config.DIALOG_STATUS['SUCCESS_DIALOG']
            else:
                self.dialog_status = dialog_config.DIALOG_STATUS['FAILED_TEMP']
                # Ask the original question again
                self.state['act'] = dialog_config.DIALOG_ACT['REQUEST']
        else:
            self.state['act'] = dialog_config.DIALOG_ACT['CLOSING']
            self.dialog_status = dialog_config.DIALOG_STATUS['SUCCESS_DIALOG']


    def response_request(self, system_action):
        if len(system_action['request_slots']) > 0:
            if 'event' not in self.state['request_slots']:
                self.dialog_status = dialog_config.DIALOG_STATUS['FAILED_TEMP']
            elif system_action['request_slots'][0] not in self.state['history_slots']:
                self.dialog_status = dialog_config.DIALOG_STATUS['PROVIDE_INFO']
            else:
                self.dialog_status = dialog_config.DIALOG_STATUS['FAILED_TEMP']
            self.state['act'] = dialog_config.DIALOG_ACT['INFORM']
            slot = system_action['request_slots'][0]  # only one slot
            # request slot in user's constraints  #and slot not in self.state['request_slots'].keys():
            if slot in self.goal['inform_slots'].keys():
                self.state['inform_slots'][slot] = self.goal['inform_slots'][slot]
                if slot in self.state['rest_slots']:
                    self.state['rest_slots'].remove(slot)
                if slot in self.state['request_slots']:
                    index = self.state['request_slots'].index(slot)
                    del self.state['request_slots'][index]
            # the requested slot has been answered
            elif slot in self.goal['request_slots'] and slot not in self.state['rest_slots'] and slot in \
                    self.state['history_slots'].keys():
                self.state['inform_slots'][slot] = self.state['history_slots'][slot]
            # request slot in user's goal's request slots, and not answered yet
            elif slot in self.goal['request_slots'] and slot in self.state['rest_slots']:
                self.state['inform_slots'][slot] = dialog_config.SPECIAL_SLOT_VALUES['I_DO_NOT_KNOW']
                if len(self.state['rest_slots']) > 0:
                    for selected_slot in self.state['rest_slots']:
                        if selected_slot in self.goal['inform_slots'].keys():
                            self.state['inform_slots'][selected_slot] = self.goal['inform_slots'][selected_slot]
                            self.state['rest_slots'].remove(selected_slot)
                            break
            else:
                self.state['inform_slots'][slot] = dialog_config.SPECIAL_SLOT_VALUES['I_DO_NOT_CARE']
                if len(self.state['rest_slots']) > 0:
                    for selected_slot in self.state['rest_slots']:
                        if selected_slot in self.goal['inform_slots'].keys():
                            self.state['inform_slots'][selected_slot] = self.goal['inform_slots'][selected_slot]
                            self.state['rest_slots'].remove(selected_slot)
                            break


    def response_closing(self, system_action):
        self.dialog_status = dialog_config.DIALOG_STATUS['SUCCESS_DIALOG']
        self.state['act'] = dialog_config.DIALOG_ACT['CLOSING']

        request_slot_set = self.state['request_slots']
        rest_slot_set = self.state['rest_slots']

        if (len(request_slot_set) > 0 or len(rest_slot_set) > 0) and \
                'event' not in system_action['inform_slots'].keys():
            self.dialog_status = dialog_config.DIALOG_STATUS['FAILED_DIALOG']

        # Find mistakes in previous turn
        sum_mistakes = 0
        for info_slot in self.state['history_slots'].keys():
            if self.state['history_slots'][info_slot] == dialog_config.SPECIAL_SLOT_VALUES['NO_VALUE_MATCH']:
                sum_mistakes += 1
            if info_slot in self.goal['inform_slots'].keys():
                if self.state['history_slots'][info_slot] != self.goal['inform_slots'][info_slot]:
                    sum_mistakes += 1
        if sum_mistakes > 1:
            self.dialog_status = dialog_config.DIALOG_STATUS['FAILED_DIALOG']


    def response_confirm_answer(self, system_action):
        ''' The agent confirm user inform slots by saying something like "Okay!" '''
        self.dialog_status = dialog_config.DIALOG_STATUS['NO_OUTCOME_YET']
        if len(self.state['request_slots']) != 0:
            if 'event' not in self.state['request_slots']:
                self.dialog_status = dialog_config.DIALOG_STATUS['FAILED_TEMP']
            self.state['act'] = dialog_config.DIALOG_ACT['REQUEST']
        elif len(self.state['rest_slots']) > 0:
            rest_inform = list(set(self.state['rest_slots']) & set(self.goal['inform_slots']))
            if len(rest_inform) > 0:
                selected_slot = random.choice(rest_inform)
            else:
                selected_slot = random.choice(self.state['rest_slots'])
            if selected_slot in self.goal['inform_slots']:
                self.state['act'] = dialog_config.DIALOG_ACT['INFORM']
                self.state['inform_slots'][selected_slot] = self.goal['inform_slots'][selected_slot]
            elif selected_slot in self.goal['request_slots']:
                self.state['act'] = dialog_config.DIALOG_ACT['REQUEST']
                self.state['request_slots'] = [selected_slot]
            self.state['rest_slots'].remove(selected_slot)
        else:
            self.state['act'] = dialog_config.DIALOG_ACT['CLOSING']


    def response_greeting(self,system_action):
        if len(self.state['request_slots']) != 0:
            if 'event' not in self.state['request_slots']:
                self.dialog_status = dialog_config.DIALOG_STATUS['FAILED_TEMP']
            self.state['act'] = dialog_config.DIALOG_ACT['REQUEST']


if __name__ == '__main__':
    user = user_simulator()
    user.start_conversation()
    user.generate_user_agenda()