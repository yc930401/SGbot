# SGbot
A task-oriented chatbot with reinforcement learning (DQN) and LSTM. 

## Introduction

This chatbot is built based on a paper called 'end-to-end task completion neural dialogue system', but I rewrote the code with Keras and adapted it to our background enviroment - Singapore event recommendation. In my opinion, it is not suitbale to be called an end-to-end system, because the system they built consists of several parts and NLU and NLG parts is not end-to-end trainable with other parts.
The components are:
1. User simulator and a real user interface
2. Natural language generator (can be sentence template filling or seq-to-seq model)
3. Natural language understanding model 
4. Dialogue manager
5. Dialogue state tracker
6. An agent with Deep Q learning

## Methodology

1. Sample and clean data from database using elastic search. 
2. Simulate the user using the sampled data, generate user agenda and randomly generate a user state (slot-value pairs).
3. Parse natural language from a real user to slot-value pairs using LSTM.
4. Update dialogue state.
5. Predict the best action with dialogue state using Deep Q Learning and update rewards.
6. Generate natural language based on agent action.

## Result

#### Simulated user
User Goal: {'request_slots': ['duration', 'is_weekend'], 'inform_slots': {'region': 'other', 'name': u'Tots Mind & Movement - $20 Trial Promo', 'event_host': u'Mums, Babies and Kids Activities (Inspire Mum & Baby)'}} </br>

User State: {'request_slots': ['event'], 'history_slots': {}, 'turn': 1, 'inform_slots': {'name': u'Tots Mind & Movement - $20 Trial Promo', 'event_host': u'Mums, Babies and Kids Activities (Inspire Mum & Baby)'}, 'rest_slots': ['region', 'duration', 'is_weekend'], 'act': 1} </br>

Agent State: {'request_slots': ['region'], 'turn': 1332, 'sentence': '', 'inform_slots': {}, 'act': 0} </br>
Episode over: False, Reward: 10 </br>

User State: {'request_slots': ['event'], 'history_slots': {'name': u'Tots Mind & Movement - $20 Trial Promo', 'event_host': u'Mums, Babies and Kids Activities (Inspire Mum & Baby)'}, 'turn': 2, 'inform_slots': {'region': 'other'}, 'rest_slots': ['duration', 'is_weekend'], 'act': 1} </br>

Agent State: {'request_slots': {}, 'turn': 1333, 'sentence': '', 'inform_slots': {'event': "I'm able to find the event.", 'name': u'Tuesday Night Badminton Game, 4 Aug, 8-10pm @ Geh Poh Ville Community Club'}, 'act': 1} </br>
Episode over: False, Reward: -10 </br>

User State: {'request_slots': ['event'], 'history_slots': {'region': 'other', 'name': u'Tots Mind & Movement - $20 Trial Promo', 'event_host': u'Mums, Babies and Kids Activities (Inspire Mum & Baby)'}, 'turn': 3, 'inform_slots': {}, 'rest_slots': ['duration', 'is_weekend'], 'act': 5} </br>

Agent State: {'request_slots': {}, 'turn': 1334, 'sentence': '', 'inform_slots': {'event': "I'm able to find the event.", 'name': u'Speed Dating Event\u2605\u2605\u260524-36F\u2605\u2605\u2605\xad28-39M'}, 'act': 1} </br>
Episode over: False, Reward: 50 </br>

User State: {'request_slots': ['is_weekend'], 'history_slots': {'region': 'other', 'name': u'Tots Mind & Movement - $20 Trial Promo', 'event_host': u'Mums, Babies and Kids Activities (Inspire Mum & Baby)'}, 'turn': 4, 'inform_slots': {}, 'rest_slots': ['duration'], 'act': 0} </br>

Agent State: {'request_slots': {}, 'turn': 1335, 'sentence': '', 'inform_slots': {'is_weekend': False}, 'act': 1} </br>
Episode over: False, Reward: 50 </br>

User State: {'request_slots': ['duration'], 'history_slots': {'region': 'other', 'name': u'Tots Mind & Movement - $20 Trial Promo', 'event_host': u'Mums, Babies and Kids Activities (Inspire Mum & Baby)'}, 'turn': 5, 'inform_slots': {}, 'rest_slots': [], 'act': 0} </br>

Agent State: {'request_slots': {}, 'turn': 1336, 'sentence': '', 'inform_slots': {'duration': "I also don't know"}, 'act': 1} </br>
Episode over: False, Reward: 100 </br>

User State: {'request_slots': [], 'history_slots': {'region': 'other', 'name': u'Tots Mind & Movement - $20 Trial Promo', 'event_host': u'Mums, Babies and Kids Activities (Inspire Mum & Baby)'}, 'turn': 6, 'inform_slots': {}, 'rest_slots': [], 'act': 4} </br>

Agent State: {'request_slots': {}, 'turn': 1337, 'sentence': '', 'inform_slots': {}, 'act': 4} </br>
Episode over: True, Reward: 100 </br>

************* simulation episode 211: Success, score: 300 </br>


## References
https://arxiv.org/pdf/1703.01008.pdf </br>
https://github.com/MiuLab/TC-Bot </br>
https://arxiv.org/pdf/1604.04562.pdf </br>
