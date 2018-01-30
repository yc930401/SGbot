import numpy as np
import dialog_config


class state_tracker():

    def __init__(self):
        self.dialog_act = dialog_config.DIALOG_ACT
        self.information_slot_names = dialog_config.INFORMATION_SLOTS
        self.request_slot_names = dialog_config.REQUEST_SLOTS
        self.initialize()


    def initialize(self):
        self.history_dictionaries = []
        self.turn_count = 0
        self.all_slots = {}

        self.all_slots['user_informed_slots'] = {}
        self.all_slots['user_current_inform'] = {}
        self.all_slots['user_current_request'] = ''
        self.all_slots['agent_informed_slots'] = {}
        self.act = 0


    def get_turn(self):
        return self.turn_count


    def update(self, agent_action=None, user_action=None):
        """ Update the state based on the latest action """
        if agent_action:
            self.act = agent_action['act']
            agent_action_values = {'turn': self.turn_count, 'speaker': "agent", 'act': agent_action['act'], \
                        'inform_slots': agent_action['inform_slots'], 'request_slots':agent_action['request_slots']}
            for slot in agent_action_values['inform_slots'].keys():
                self.all_slots['agent_informed_slots'][slot] = agent_action_values['inform_slots'][slot]
            self.history_dictionaries.append(agent_action_values)

        elif user_action:
            self.act = user_action['act']
            user_action_values = {'turn': self.turn_count, 'speaker': "user", 'request_slots': user_action['request_slots'],\
                                  'inform_slots': user_action['inform_slots'], 'act': user_action['act']}
            # clear old state
            self.all_slots['user_current_inform'].clear()
            self.all_slots['user_current_request'] = ''
            for slot in user_action['inform_slots'].keys():
                self.all_slots['user_informed_slots'][slot] = user_action['inform_slots'][slot]
            if len(user_action['request_slots']) > 0:
                self.all_slots['user_current_request'] = user_action['request_slots'][0]
            self.history_dictionaries.append(user_action_values)
        self.turn_count += 1


    def get_agent_input_vector(self):
        ''' Vector format: (user_informed_slots, user_current_inform, agent_informed_slots, user_current_request) '''

        vector = np.zeros((len(self.information_slot_names)*3 + len(self.request_slot_names) + len(self.dialog_act), 1))
        inform_index_table = {value: index for index, value in enumerate(self.information_slot_names)}
        request_index_table = {value: index for index, value in enumerate(self.request_slot_names)}
        for slot in self.all_slots['user_informed_slots'].keys():
            index = inform_index_table[slot]
            vector[index] += 1
        for slot in self.all_slots['user_current_inform']:
            index = inform_index_table[slot] + len(inform_index_table)
            vector[index] += 1
        for slot in self.all_slots['agent_informed_slots'].keys():
            index = request_index_table[slot] + len(inform_index_table)*2
            vector[index] += 1

        if len(self.all_slots['user_current_request']) != 0:
            index = request_index_table[self.all_slots['user_current_request']] + len(inform_index_table)*3
            vector[index] += 1
        index = self.act + len(inform_index_table)*3 + len(self.request_slot_names)
        vector[index] += 1
        return vector