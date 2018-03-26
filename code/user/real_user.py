import dialog_config


class real_user():

    def __init__(self):
        self.sentence = ''
        self.episode_over = False
        self.dialog_status = dialog_config.DIALOG_STATUS['NO_OUTCOME_YET']

    def generate_user_response(self):
        action = {}
        action['act'] = ''
        action['inform_slots'] = ''
        action['request_slots'] = ''
        action['turn'] = ''
        action['sentence'] = self.sentence

        return action, self.episode_over, self.dialog_status


    def update_sentence(self, sentence):
        self.sentence = sentence