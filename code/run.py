import time
from user_simulator import user_simulator
from real_user import real_user
from DQN_agent import DQNAgent
from dialog_manager import dialog_manager

class responder():

    def __init__(self, mode=0):
        self.mode = mode
        agent = DQNAgent(mode=self.mode)
        user = user_simulator()
        self.manager = dialog_manager(agent, user, self.mode, maximum_turn = 20)
        self.simulation_epoch_size = 800


    def run(self):
        successes = 0
        cumulative_reward = 0
        cumulative_turns = 0

        res = {}
        if self.mode:
            self.manager.initialize()
            episode_over = False
            while (not episode_over):
                episode_over, reward, sentence = self.manager.next_turn()
                cumulative_reward += reward
                if episode_over:
                    if reward > 0:
                        successes += 1
                        print("************* real episode Success" )
                    else:
                        print("************* real episode Fail")
                    #cumulative_turns += self.manager.state_tracker.turn_count

        else:
            for episode in range(self.simulation_epoch_size):
                episode_reward = 0
                self.manager.initialize()
                episode_over = False
                while (not episode_over):
                    episode_over, reward, sentence = self.manager.next_turn()
                    cumulative_reward += reward
                    episode_reward += reward
                    if episode_over:
                        if reward > 0:
                            successes += 1
                            print("************* simulation episode {}: Success, score: {}\n" .format(episode, episode_reward))
                        else:
                            print("************* simulation episode {}: Fail, score: {}\n".format(episode, episode_reward))
                        cumulative_turns += self.manager.state_tracker.turn_count

            res['success_rate'] = float(successes) / self.simulation_epoch_size
            res['ave_reward'] = float(cumulative_reward) / self.simulation_epoch_size
            res['ave_turns'] = float(cumulative_turns) / self.simulation_epoch_size
            print('simulation success rate {}, ave reward {}, ave turns {}'.format( \
                res['success_rate'], res['ave_reward'], res['ave_turns']))
        return sentence


if __name__ == '__main__':
    # training process
    '''
    res = responder()
    start_time = time.time()
    res.run()
    print("Training time: {} hours ".format((time.time() - start_time) / 3600))
    '''

    # testing process
    res = responder(mode=1)
    start_time = time.time()
    res.run()

