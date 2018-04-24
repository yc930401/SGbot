from real_user import real_user
from state_tracker import state_tracker
from DQN_agent import DQNAgent
from natural_language_understanding import NL_understanding as NLU
from natural_language_generator_rule import NL_rule_generator as NLG
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters
import warnings
warnings.filterwarnings("ignore")

nlu = NLU()
nlg = NLG()
agent = DQNAgent(mode=1)
agent.initialize()


# functions
def start(bot, update):
    print('start')
    user = real_user()
    state_keeper = state_tracker()
    state_keeper.initialize()
    bot_sessions[update.message.chat_id] = user
    user_states[user] = state_keeper
    update.message.reply_text('Hello World!')


def hello(bot, update):
    print('hello')
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


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


def reply(bot, update):
    print('reply')
    if update.message.chat_id in bot_sessions.keys():
        user = bot_sessions[update.message.chat_id]
        state_keeper = user_states[user]
    else:
        user = real_user()
        state_keeper = state_tracker()
        state_keeper.initialize()
        bot_sessions[update.message.chat_id] = user
        user_states[user] = state_keeper
    msg = update.message['text']
    print(msg)
    response = respond(msg, user, state_keeper)
    # return response
    bot.send_message(chat_id=update.message.chat_id, text=response)



if __name__ == '__main__':
    '''
    user = real_user()
    state_keeper = state_tracker()
    state_keeper.initialize()
    respond(u'i want to find an event near SMU', user, state_keeper)
    '''
    bot_sessions = {}
    user_states = {}

    updater = Updater('442416167:AAHDdAwqrB8D91rbegrWI17zyIxaDwtkzPI')
    message_handler = MessageHandler(Filters.text, reply)
    start_handler = CommandHandler('start', start)
    hello_handler = CommandHandler('hello', hello)

    # adding handlers
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(hello_handler)

    print('listening')
    # listen to requests
    updater.start_polling()

