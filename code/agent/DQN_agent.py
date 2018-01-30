import random
import numpy as np
from operator import itemgetter
from collections import deque
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
import dialog_config
import db_helper
from natural_language_generator_rule import NL_rule_generator
from keras import initializers


class DQNAgent:
    def __init__(self, mode):
        self.mode = mode
        self.memory = deque(maxlen=2000)
        self.gamma = 0.2  # discount rate 0.95
        self.epsilon_min = 0.01
        if self.mode:
            self.epsilon = self.epsilon_min
        else:
            self.epsilon = 1.0  # exploration rate
        self.epsilon_decay = 0.9995
        self.learning_rate = 0.001
        self.turn = 1
        self.batch_size = 32
        self.dialog_act = dialog_config.DIALOG_ACT
        self.state_size = len(dialog_config.INFORMATION_SLOTS) * 3 + len(dialog_config.REQUEST_SLOTS) + len(
            self.dialog_act)
        self.action_size = len(dialog_config.REQUEST_SLOTS) + len(dialog_config.INFORMATION_SLOTS)
        self.model = self._build_model()
        self.nlg = NL_rule_generator()


    def initialize(self):
        self.proposed_event = []
        self.episode_over = False

    def keras_initializer(self):
        pass

    def _build_model(self):
        # Neural Net for Deep-Q learning Model
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu',
                        kernel_initializer=initializers.RandomNormal(stddev=0.001)))
        model.add(Dense(48, activation='relu'))
        model.add(Dense(48, activation='relu'))
        model.add(Dense(96, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))
        '''
        if len(self.memory) > 2000:
            self.memory.sort(key=itemgetter(2), reverse = True)
            self.memory = self.memory[:2000]# + self.memory[-700:]
        '''

    def act(self, agent_input):
        if np.random.rand() <= self.epsilon:
            random_values = np.zeros((self.action_size, 1))
            #if np.random.rand() > self.epsilon*0.5:
            random_index = random.randrange(self.action_size)
            random_values[random_index] = 1
            #else: # recommend event
            #    random_values[len(dialog_config.REQUEST_SLOTS)-1] = 1
            return random_values.argmax()
        act_values = self.model.predict(agent_input)
        return np.argmax(act_values[0])  # returns action

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = (reward + self.gamma *
                          np.amax(self.model.predict(next_state)[0]))
            target = (reward + self.gamma * np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
        #if self.turn % 600 == 0 and self.turn < 15000:
        #    self.epsilon = self.epsilon_max

    def load(self, name):
        #if os.path.exists(name):
        try:
            self.model.load_weights(name)
        except:
            pass

    def save(self, name):
        self.model.save_weights(name, overwrite=True)

    def generate_agent_response(self, agent_input, user_informed_slots, user_act):
        action = None
        self.load("dqn.h5")
        # fill in state according to action
        response_action = {}
        response_action['inform_slots'] = {}
        response_action['request_slots'] = {}
        if user_act == dialog_config.DIALOG_ACT["CLOSING"]:
            response_action['act'] = dialog_config.DIALOG_ACT["CLOSING"]
            self.episode_over = True
        elif sum(agent_input) == 0:
            response_action['act'] = dialog_config.DIALOG_ACT["GREETING"]
        elif user_act == dialog_config.DIALOG_ACT["THANK"]:
            response_action['act'] = dialog_config.DIALOG_ACT["THANK"]
        else:
            action = int(self.act(agent_input.reshape(1, -1)))
            if action in range(0,len(dialog_config.REQUEST_SLOTS)):
                response_action['act'] = dialog_config.DIALOG_ACT["INFORM"]
                slot = dialog_config.REQUEST_SLOTS[action]
                response_action['inform_slots'][slot] = True
            elif action in range(len(dialog_config.REQUEST_SLOTS), self.action_size-2):
                response_action['act'] = dialog_config.DIALOG_ACT["REQUEST"]
                slot = dialog_config.INFORMATION_SLOTS[action-(len(dialog_config.REQUEST_SLOTS))]
                response_action['request_slots'] = [slot]
            else: # action == self.action_size-1:
                response_action['act'] = dialog_config.DIALOG_ACT["CONFIRM_ANSWER"]


        # if inform, search db
        if response_action['act'] == dialog_config.DIALOG_ACT['INFORM']:
            self.db_search(response_action, user_informed_slots)
        response_action['turn'] = self.turn
        response_action['sentence'] = self.generate_sentence(response_action)
        self.turn += 1

        if not self.mode and len(self.memory) > self.batch_size and not self.episode_over:
            for i in range(15):
                self.replay(self.batch_size)
        if not self.mode:
            self.save("dqn.h5")
        return response_action, action, self.episode_over


    def generate_sentence(self, response_action):
        return self.nlg.convert_state_to_nl(response_action)

    def db_search(self, response_action, user_informed_slots):
        if "event" in response_action['inform_slots'].keys():

            results_10 = db_helper.search(user_informed_slots)
            if len(self.proposed_event) > 0:
                for proposed in self.proposed_event:
                    if proposed in results_10:
                        index = results_10.index(proposed)
                        del results_10[index]
            if len(results_10) > 0:
                result = random.choice(results_10)
                self.proposed_event.append(result)
                response_action['inform_slots']['event'] = dialog_config.SPECIAL_SLOT_VALUES['EVENT_AVAILABLE']
                response_action['inform_slots']['name'] = self.proposed_event[-1]['name']
            else:
                response_action['inform_slots']['event'] = dialog_config.SPECIAL_SLOT_VALUES['NO_VALUE_MATCH']
        if len(self.proposed_event) > 0:
            for key in response_action['inform_slots'].keys():
                if key != 'event':
                    try:
                        response_action['inform_slots'][key] = self.proposed_event[-1][key]
                    except:
                        response_action['inform_slots'][key] = dialog_config.SPECIAL_SLOT_VALUES['I_DO_NOT_KNOW']
        return
