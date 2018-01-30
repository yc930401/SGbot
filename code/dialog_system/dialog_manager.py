from state_tracker import state_tracker
import dialog_config


class dialog_manager:
    """ A dialog manager to mediate the interaction between an agent and a customer """

    def __init__(self, agent, user, mode, maximum_turn):
        self.mode = mode
        self.max_turn = maximum_turn
        self.agent = agent
        self.user = user
        self.state_tracker = state_tracker()
        self.user_action = None
        self.agent_action = None
        self.reward = 0


    def initialize(self):
        ''' New Dialog Preparation '''

        self.reward = 0
        self.last_reward = 0
        self.episode_over = False
        self.state_tracker.initialize()
        # generate new user agenda
        self.user_action, dialog_status = self.user.generate_user_agenda(max_turn = self.max_turn)
        # update user state
        self.state_tracker.update(user_action=self.user_action)
        self.agent.initialize()

    def next_turn(self, record_training_data=True):
        """ Initiates each subsequent exchange between agent and user (agent first) """
        # agent action
        agent_state = self.state_tracker.get_agent_input_vector()
        self.agent_action, action, self.episode_over = self.agent.generate_agent_response(agent_state, \
                self.state_tracker.all_slots['user_informed_slots'], self.state_tracker.act)
        print('Agent State: {}'.format(self.agent_action))
        self.state_tracker.update(agent_action=self.agent_action)

        self.user_action, dialog_status, user_state = self.user.generate_user_response(self.agent_action)
        self.reward = self.reward_function(self.user_action, dialog_status, self.state_tracker.get_turn())
        if not self.episode_over:
            print('Episode over: {}, Reward: {}\nUser State: {}'.format(self.episode_over, self.reward, user_state))
        else:
            print('Episode over: {}, Reward: {}'.format(self.episode_over, self.reward))
        agent_state_next = self.state_tracker.get_agent_input_vector()
        #if (self.reward > self.last_reward or self.reward >= 10) and action is not None:
        if action is not None and not self.mode:
            self.agent.remember(agent_state.reshape(1,-1), action, self.reward, \
                            agent_state_next.reshape(1,-1), self.episode_over)
        self.last_reward = self.reward
        if self.episode_over != True:
            self.state_tracker.update(user_action=self.user_action)
        return (self.episode_over, self.reward, self.agent_action['sentence'])


    def reward_function(self, user_action, dialog_status, turn):
        """ Reward based on the dialog_status """
        reward = dialog_status
        #if dialog_status == dialog_config.DIALOG_STATUS["FAILED_DIALOG"] and \
        #    user_action == dialog_config.DIALOG_ACT["CLOSING"]:
        #    reward -= (self.max_turn*2 - turn) * 60 # if 50, the same as respond wrongly.
        return reward