import json
import dialog_config


class NL_rule_generator():
    # init file path and load data
    def __init__(self):
        self.language_pairs_path = 'language_pairs.json'
        self.language_pairs = self.__load_event_Data__()


    def __load_event_Data__(self):
        data = json.load(open(self.language_pairs_path, 'r'))
        for key in data['dia_acts'].keys():
            for ele in data['dia_acts'][key]:
                ele['nl']['usr'] = ele['nl']['usr'].encode('utf-8')  # encode issue
                ele['nl']['agt'] = ele['nl']['agt'].encode('utf-8')  # encode issue
        return data


    def convert_state_to_nl(self, state):
        sentence = ""
        base = ""
        turn_msg = state['turn']
        # remove slot with value 'I do not care'
        if state['act'] == dialog_config.DIALOG_ACT['INFORM'] and 'event' in state['inform_slots'].keys() \
                and state['inform_slots']['event'] != dialog_config.SPECIAL_SLOT_VALUES['NO_VALUE_MATCH']:
            for slot,value in state['inform_slots'].items():
                if value == dialog_config.SPECIAL_SLOT_VALUES['I_DO_NOT_CARE']:
                    del state['inform_slots'][slot]
                    base = "I do not care about {}. ".format(slot)
                if value == dialog_config.SPECIAL_SLOT_VALUES['I_DO_NOT_KNOW']:
                    del state['inform_slots'][slot]
                    base = "I also don't know about {}. ".format(slot)
        # match slots and fill sentence
        if state['act'] in self.language_pairs['dia_acts'].keys():
            for ele in self.language_pairs['dia_acts'][state['act']]:
                if set(ele['inform_slots']) == set(state['inform_slots'].keys()) \
                        and set(ele['request_slots']) == set(state['request_slots'].keys()):
                    sentence = self.nl_slot_filling(base, state, ele['nl'][turn_msg])
                    break
        # if fail to find an event
        if state['act'] == dialog_config.DIALOG_ACT['INFORM'] and 'event' in state['inform_slots'].keys() \
                and state['inform_slots']['event'] == dialog_config.SPECIAL_SLOT_VALUES['NO_VALUE_MATCH']:
            sentence = "Oh sorry, there is no suitable event for you."

        return sentence


    def nl_slot_filling(self, base, state, template_sentence):
        """ Replace the slots with its values """
        sentence = base + template_sentence
        counter = 0
        for slot in state['inform_slots'].keys():
            slot_val = state['inform_slots'][slot]
            if slot_val == dialog_config.SPECIAL_SLOT_VALUES['NO_VALUE_MATCH']:
                sentence = "Sorry, {} is not available now.".format(slot)
                break
            sentence = sentence.replace('$' + slot + '$', slot_val, 1)

        return sentence


if __name__ == '__main__':
    nlg = NL_rule_generator()