import dialog_config


class real_user():

    def __init__(self, sentence=''):
        self.sentence = sentence
        self.episode_over = False
        self.dialog_status = dialog_config.DIALOG_STATUS['NO_OUTCOME_YET']
        self.turn = 0
        self.history_slots = {}

    def generate_user_response(self):
        action = {}
        action['act'] = -1
        action['inform_slots'] = {}
        action['request_slots'] = []
        action['turn'] = self.turn
        action['sentence'] = self.sentence
        action['history_slots'] = self.history_slots
        self.history_slots = action['inform_slots']

        return action, self.episode_over, self.dialog_status


    def update_sentence(self, sentence):
        self.sentence = sentence
        self.turn += 1