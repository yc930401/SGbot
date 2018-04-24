from real_user import real_user
from state_tracker import state_tracker
from DQN_agent import DQNAgent
from natural_language_understanding import NL_understanding as NLU
from natural_language_generator_rule import NL_rule_generator as NLG

nlu = NLU()
nlg = NLG()
agent = DQNAgent(mode=1)
agent.initialize()


def respond(msg, user, state_keeper):
    # user turn
    user.update_sentence(msg)
    user_action, episode_over, dialog_status = user.generate_user_response()
    user_action = nlu.convert_nl_to_state(user_action)
    print('User State: {}\nEpisode_over: {}'.format(user_action, episode_over))
    state_keeper.update(user_action=user_action)
    # agent turn
    agent_state = state_keeper.get_agent_input_vector()
    agent_action, action, episode_over = agent.generate_agent_response(agent_state, \
                                                                       state_keeper.all_slots['user_informed_slots'],
                                                                       state_keeper.act)
    if nlg.convert_state_to_nl(agent_action) != '':
        agent_action['sentence'] = nlg.convert_state_to_nl(agent_action)
    else:
        agent_action['sentence'] = 'Response not available ...'
    print('Agent State: {}'.format(agent_action))
    state_keeper.update(agent_action=agent_action)
    return agent_action['sentence']

if __name__ == '__main__':
    user = real_user()
    state_keeper = state_tracker()
    state_keeper.initialize()
    while True:
        msg = raw_input('User input: ')
        respond(msg, user, state_keeper)