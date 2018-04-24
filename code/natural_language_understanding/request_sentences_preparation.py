import numpy as np
import dialog_config

request_venue_name = [
    "I want to know the venue of the event.",
    "I want to know the venue of it.",
    "May I have the venue of the event?",
    "May I know the venue of the event?",
    "May I know where it will be held?",
    "May I know where it'll be held?",
    "May I know where it is held?",
    "May I know where can I find the event?",
    "May I know the place it will be held?",
    "May I know the place it'll be held?",
    "May I know the place of the event?",
    "May I know the place of it?",
    "May I know the place the event will be held?",
    "Can I know which venue will it be held?",
    "Can I know which venue will it be held?",
    "Can I know which venue will the event be held?",
    "Can you tell me the venue of the event?",
    "Can you tell me the venue of it?",
    "Can you tell me the place of the event?",
    "Can you tell me the place of it?",
    "Where will the event be held?",
    "Where will it be held?",
    "Where will the event be organised?",
    "Where can I find the group?",
    "Where can I find the organiser?",
    "Where can I find the event?",
    "Where is it?",
    "Can you help me check the venue of the event?",
    "Can you help me check the venue of it?",
    "Can you help me check the place of the event?",
    "Can you help me check the place of it?",
    "Tell me the venue of that event.",
    "Tell me the venue of it.",
    "Could you please tell me the venue of the event?",
    "Could you please tell me the venue of it?",
    "Could you please help me check the venue of the event?",
    "Please tell me the venue of the event.",
    "Please tell me the venue of it.",
    "Please tell me where it will be held.",
    "Please tell me where it'll be held.",
    "Please tell me the place of the event.",
    "Which venue?",
    "Venue?"
]


request_address = [
    "May I know the address of it?",
    "May I know the address of the event?",
    "May I know the address of the building?",
    "May I know the exact place where it will be held?",
    "May I have the place where it'll be held?",
    "May I have the address of the event?",
    "May I have the address of it?",
    "Can you tell me the address?",
    "Can you tell me the address of it?",
    "Can you tell me the address of the event you recommended?",
    "Can you tell me the exact place of it?",
    "Could you please tell me the address?",
    "Could you please tell me the address of it?",
    "Could you please tell me the address of the event?",
    "Could you please tell me the exact address?",
    "I want to know the address.",
    "I want to know the address of the event you recommended.",
    "I want to know the address of the event.",
    "I want to know the address of it.",
    "I want to know the address.",
    "I want to know its address.",
    "Can you help me check the address?",
    "Can you help me check the address of it?",
    "Can you help me with the address of it?",
    "Can you help me check the place of the event?",
    "Can you help me check the place it'll be held?",
    "Can you help me check the place it will be held?",
    "Tell me the place it will be held.",
    "Tell me the address.",
    "Tell me the address of the event.",
    "Tell me the address of it.",
    "Please tell me the address of it.",
    "Please tell me the exact place that it'll be held.",
    "Please tell me the exact place that it will be held.",
    "Where is it?",
    "Where will it be held?",
    "Where can I find it?",
    "The address?",
    "The address of it?",
    "Address?",
    "Where?"
]


request_event_host = [
    "Which group it belongs to?",
    "Which group the event belongs to?",
    "Which group will organise the event?",
    "Who is the organiser?",
    "Who's the organiser?",
    "Who will organise it?",
    "Who will organise the event?",
    "Who organise the event?",
    "Who organise it?",
    "May I know the organiser?",
    "May I know the organiser of it?",
    "May I know which group holds it?",
    "May I know which group will hold it?",
    "May I know the group of the event?",
    "May I know which group will hold the event?",
    "May I know which group holding the event?",
    "May I know which group organising the event?",
    "May I know which group that organise the event?",
    "May I know the group of it?",
    "Can I have the name of the group?",
    "Can I know which group that holds it?",
    "Can I know the group organising it?",
    "Can I know the group holding it?",
    "Tell me the group that holds the event.",
    "Tell me which group it belongs to?",
    "Tell me the host of the event.",
    "Tell me the organiser of the event.",
    "Please tell me who will organise it?",
    "Please tell me who will organise the event.",
    "Please tell me who will hold the event.",
    "Please tell me the host of tht event.",
    "Can you help me check the host of that event?",
    "Could you please help me check the organiser of the event?",
    "Could you please help me check the organiser of it?",
    "Could you please help me check the organiser?",
    "Could you tell me the group that will hold the event?",
    "Could you tell me the group that will organise the event?",
    "The organiser?",
    "The group?"
]


request_date_start = [
    "When will it be held?",
    "When will the event be held?",
    "When is it?"
    "When is the event?",
    "When is the event start?",
    "When will the event begin?",
    "When will it begin?",
    "On which day will it be held?",
    "On which day will the event be held?",
    "May I know the date of the event?",
    "May I know when will it be held?",
    "May I know when is it?",
    "May I have the date of the event?",
    "May I have the date of it?",
    "May I have the date?",
    "When?",
    "Which day will it be held?",
    "Which day?",
    "The date?",
    "Its date?",
    "Date?",
    "Tell me the date.",
    "Tell me when is it?",
    "Tell me when.",
    "Tell me when will it begin.",
    "Tell me the start date.",
    "Could you help me check the date?",
    "Could you tell me when is it?",
    "Could you please tell me the date?",
    "Could you please tell me the date of it?",
    "Could you please tell me when is it?",
    "Please tell me the date.",
    "Help me check the date.",
    "Help me check when is it.",
    "Help me check the date of the event."
]


request_time = [
    "Can you tell me the time?",
    "Can you tell me the start time of the event?",
    "Can you tell me the start time of it?",
    "When will it start?",
    "When will it begin",
    "When will the event begin?",
    "The time?"
    "Time?",
    "What time?",
    "The exact time?",
    "The start time?",
    "Could you please tell me the time it begins?",
    "Could you please tell the time of the event?",
    "Could you please tell me the time of it?",
    "Could you tell me the start time of it?",
    "Tell me the time of it.",
    "Tell me the time.",
    "Tell me the time of the event.",
    "Tell me the time it begins?",
    "Tell me the time it will begin?",
    "Tell me when is the event.",
    "Could you please tell me the time?",
    "Could you please tell me the time of it?",
    "Could you please tell me the time of the event you recommended?",
    "Please tell me the exact time.",
    "Please tell me the time it begins.",
    "Please tell me the time of it.",
    "On what time?",
    "Could you please help me check the time?",
    "Could you please help me check the time of it?",
    "Could you check the time of it?",
    "Could you check when it begins?",
    "Could you check when it will begin?"
]


request_price = [
    "Price?",
    "The price?"
    "The price of it?",
    "The price of the event?",
    "Is it free?",
    "Is it free or not?",
    "Free?",
    "How much?",
    "How much is it?",
    "How much does it take?",
    "Fee?",
    "Is it free or not?",
    "Is it a free event?",
    "Help me check the price.",
    "Can you tell me the price?",
    "Can you tell me the fee?",
    "What's the price of it?",
    "What's the fee of it?",
    "What's the price of the event?",
    "What's the fee of the event?",
    "What's the price?",
    "What's the fee?",
    "Is it expensive?",
    "Is it cheap?",
    "Do I need to pay?",
    "How much do I need to pay?",
    "How much to pay?",
    "Do you know how much is the fee?",
    "Do you know the price?",
    "I want to know the price",
    "I want to know the fee.",
    "Tell me if it's expensive?",
    "Tell me if it is cheap?",
    "Tell me if it is free?",
    "Can you help me check the price?",
    "Can you help me check the fee?",
    "Could you please help me check the price?",
    "Could you please help me check the fee?",
    "Could you please help me check if it is free?",
    "Could you please help me check how much is it?"
]


request_is_weekend = [
    "Is it in the weekend?",
    "Is it a weekend event?",
    "Is it a weekday event?",
    "On weekday or weekend?",
    "Is it occurring on weekend?",
    "Is it organised on weekend?",
    "Is it occurring on weekday?",
    "Is it organised on weekday?",
    "Is it on weekend?",
    "Is it on weekday?",
    "Can you tell me if it is on weekend?",
    "Can you tell me if it is on weekday?",
    "Can you tell me if it is a weekend event?",
    "Can you tell me if it is a weekday event?",
    "Could you please help me check if it is on weekday?",
    "Could you please help me check if it is on weekend?",
    "Could you please help me check if it is a weekday event?",
    "Could you please help me check if it is a weekend event?",
    "Tell me if it is on weekday.",
    "Tell me if it's on weekday.",
    "Tell me if it is on weekend.",
    "Tell me if it's on weekend.",
    "May I know if it is on weekday?",
    "May I know if it's on weekday?",
    "May I know if it is on weekend?",
    "May I know if it's on weekend?",
    "Please tell me if it's a weekday event?",
    "Please tell me if it's a weekend event?",
    "Please tell me if it is on weekday?",
    "Please tell me if it is on weekend?",
    "On weekday?",
    "Weekday?",
    "On weekend?",
    "Weekend?"
]


request_part_of_day = [
    "Is it in the morning?",
    "Is it in the afternoon?",
    "Is it in the evening?",
    "Is it at night?",
    "Is it a morning event?",
    "Is it a afternoon event?",
    "Is it a evening event?",
    "Is it a night event?",
    "Will it be held in the evening?",
    "Will it be held in the afternoon?",
    "Will it be held in the morning?",
    "Will it be held at night?",
    "Will it be held after dawn?",
    "Will it be held in the day break?",
    "Will it be organised in the evening?",
    "Will it be organised in the afternoon?",
    "Will it be organised in the morning?",
    "Will it be organised at night?",
    "Will it be organised after dawn?",
    "Will it be organised in the day break?",
    "Can you tell me if it is organised in the morning?",
    "Can you tell me if it is organised in the evening?",
    "Can you tell me if it is organised in the afternoon?",
    "Can you tell me if it is a morning event?",
    "Can you tell me if it is an evening event?",
    "Can you tell me if it is an afternoon event?",
    "Morning?",
    "Afternoon?",
    "Evening?",
    "At night?",
    "Noon?",
    "In the day break?",
    "After dawn?",
    "At mid night?",
    "Midnight?",
    "In the mid day?"
]


request_event_url = [
    "Tell me the url.",
    "Tell me the url of the event.",
    "Tell me the link.",
    "Tell me the link of it.",
    "Tell me the link of the event.",
    "Tell me the web page of it.",
    "Tell me the wesite.",
    "The url?",
    "Url?",
    "The link?",
    "The link of it?",
    "The website?",
    "The web page?",
    "Tell me where I can find more information about the event.",
    "Tell me where I can find more info about the event.",
    "Could you please tell me the link of the event?",
    "Could you please tell me the url of the event?",
    "Could you please tell me the url?",
    "Could you help me check the url?",
    "Could you help me check the link?",
    "Please tell me the url.",
    "Please tell me the url of the event.",
    "Please tell me the url of it.",
    "Please tell me the link.",
    "Please tell me the link of it.",
    "Please tell me the link of the event.",
    "Please tell me the web page.",
    "Please tell me the website.",
    "Please tell me the website to find more info.",
    "Please tell me their website to find more information.",
    "Please tell me the link of the event to find more info.",
    "Please tell me the url of the event to find more information.",
    "Tell me the url of the event to find more info.",
    "Tell me the link of the event to find more information.",
    "Tell me their website to find more information.",
    "Tell me their website to find more info.",
    "I want to know more about the event."
]


request_duration = [
    "How long will it be?",
    "How long will it last?",
    "How long?",
    "The duration?",
    "The time it will last?",
    "How long is it?",
    "Will it finish in 2 hours?",
    "Will it finish in 1 hour?",
    "When will it finish?",
    "When will it end?",
    "How long does it take?",
    "Can you tell me how long does it take?",
    "Can you tell me how long is it?",
    "Can you tell me how long does the event take?",
    "Tell me when will it finish?",
    "Tell me how long does it take?",
    "Tell me when will it end?",
    "Tell me the time it ends?",
    "Tell me the time it finishes?",
    "Tell me the time it will end?",
    "Tell me the time it will finish?",
    "Could you please tell me when will it finish?",
    "Could you please tell me when will it end?",
    "Can you help me check how long will it take?",
    "Can you help me check how long will it last?",
    "Please tell me the duration of the event.",
    "Please tell me the duration of it.",
    "Please tell me how long will it last.",
    "Please tell me when will it finish?",
    "Please tell me when will it end?",
    "Please tell me how long does it take?",
    "Please tell me how long will it take?",
    "Please tell me the time it ends.",
    "The time it finishes?",
    "The time it ends?"
]


greeting = [
    "Good morning!",
    "Good afternoon!",
    "Good evening!",
    "Good morning! Nice to see you.",
    "Good afternoon! Nice to see you.",
    "Good evening! Nice to see you.",
    "Good day!",
    "Hello",
    "Hi",
    "How are you!",
    "How do you do!",
    "How are things?",
    "Morning!",
    "Afternoon!",
    "Evening!",
    "Nice day today!",
    "How is it going?",
    "How are you doing!",
    "How's everything going?",
    "Long time no see.",
    "Hey!",
    "Hey man!",
    "What's up?",
    "Hiya!",
    "Yo!",
    "Howdy!",
    "Sup?"
]


deny = [
    "Sorry, I don't like it.",
    "Sorry, I don't like the event you recommended.",
    "Sorry, I dislike the event.",
    "Sorry, I dislike it.",
    "Sorry, I don't think it is suitable for me.",
    "Sorry, I don't think it is a suitable event.",
    "Can you recommend something else?",
    "Can you recommend another event?",
    "Can you recommend another one?",
    "Recommend me something else.",
    "Recomemnd another one.",
    "Do you have other events to recommend?",
    "Do you have other suggestions?",
    "Anything else?",
    "Something else?",
    "Other events?",
    "Other suggestions?",
    "Sorry, I don't like it. Can you recommend something else?",
    "Sorry, I don't like it. Do you have other suggestions?",
    "Sorry, I dislike like it. Can you recommend something else?",
    "Sorry, I dislike like it. Do you have other suggestions?",
    "Sorry, I don't like it. Do you have another event in mind?",
    "Sorry, I dislike like it. Do you have other suggestions?",
    "Sorry, I don't like it. Do you know any other event?",
    "Sorry, I dislike like it. Do you have any other suggestions?",
    "No",
    "No, I don't like it!",
    "No, I dislike it!",
    "No, any other suggestions?",
    "No, I hate it!",
    "No no no!",
    "No, other events?",
    "No, other recommendations?",
    "That's not good!",
    "I hate it!",
    "I dislike it",
    "I don't like it",
    "I don;t think it is a good idea.",
    "That's not good! Anything else?",
    "I dislike it! Any other events?",
    "I dislike it! Tell me something else!",
    "I don't like it! Any other events?",
    "I don't like it! Tell me something else!",
    "I hate it! Any other events?",
    "I hate it! Tell me something else!",
    "Tell me something else!",
    "Tell me about other events!",
    "No way.",
    "That's too bad. Anything else you want to recommend?",
    "What else?",
    "Bad idea!",
    "I dislike the group.",
    "I don't like the group",
    "Why not recommend something else?",
    "Why not recommend another event?",
    "Why not recommend something interesting?",
    "Recommend something interesting."
]

closing = [
    "Nice talking to you.",
    "Have a nice day!",
    "Bye!",
    "bye-bye",
    "bye bye",
    "See you later",
    "See you.",
    "Goodbye.",
    "Nice to meet you.",
    "Ok, nice. Bye.",
    "Talk to you later.",
    "Take care!",
    "Ok, nice. Enjoy your day!"
]

thank = [
    "Thank you!",
    "Thanks!",
    "Thanks a lot!",
    "Thank you for your help!",
    "Thank you very much!",
    "Thank you so much!",
    "Thanks for helping!",
    "Thanks for helping me.",
    "Thanks, you're really nice!",
    "Ok, thank you!",
    "Thank you! Yo are really helpful!",
    "Tou are really helpful!",
    "Nice having you here."
]


file_1 = open('User_intent.txt', 'r')
file_2 = open('request_slot_classification.txt', 'w')

inform_data = file_1.read().split('\n')
index = [i for i in range(int((len(inform_data)-1)/2))]
np.random.shuffle(index)
sentence_index = [2*i for i in index[:8000]]
label_index = [2*i+1 for i in index[:8000]]
inform_sentences = [inform_data[i] for i in sentence_index]
inform_labels = [inform_data[i] for i in label_index]
file_1.close()

file_1 = open('User_intent.txt', 'w')
for i in range(len(inform_labels)):
    file_1.write(inform_sentences[i] + '\n')
    file_1.write(inform_labels[i] + '\n')

for sentence in request_venue_name:
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "").replace(',', '')
    for i in range(20):
        file_1.write(sentence + '\n')
        file_1.write(str(dialog_config.DIALOG_ACT['REQUEST']) + '\n')
    file_2.write(sentence + '\n')
    file_2.write("venue_name" + '\n')

for sentence in request_address:
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "").replace(',', '')
    for i in range(20):
        file_1.write(sentence + '\n')
        file_1.write(str(dialog_config.DIALOG_ACT['REQUEST']) + '\n')
    file_2.write(sentence + '\n')
    file_2.write("address" + '\n')

for sentence in request_event_host:
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "").replace(',', '')
    for i in range(20):
        file_1.write(sentence + '\n')
        file_1.write(str(dialog_config.DIALOG_ACT['REQUEST']) + '\n')
    file_2.write(sentence + '\n')
    file_2.write("event_host" + '\n')

for sentence in request_date_start:
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "").replace(',', '')
    for i in range(20):
        file_1.write(sentence + '\n')
        file_1.write(str(dialog_config.DIALOG_ACT['REQUEST']) + '\n')
    file_2.write(sentence + '\n')
    file_2.write("date_start" + '\n')

for sentence in request_time:
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "").replace(',', '')
    for i in range(20):
        file_1.write(sentence + '\n')
        file_1.write(str(dialog_config.DIALOG_ACT['REQUEST']) + '\n')
    file_2.write(sentence + '\n')
    file_2.write("time" + '\n')

for sentence in request_price:
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "").replace(',', '')
    for i in range(20):
        file_1.write(sentence + '\n')
        file_1.write(str(dialog_config.DIALOG_ACT['REQUEST']) + '\n')
    file_2.write(sentence + '\n')
    file_2.write("price" + '\n')

for sentence in request_is_weekend:
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "").replace(',', '')
    for i in range(20):
        file_1.write(sentence + '\n')
        file_1.write(str(dialog_config.DIALOG_ACT['REQUEST']) + '\n')
    file_2.write(sentence + '\n')
    file_2.write("is_weekend" + '\n')

for sentence in request_part_of_day:
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "").replace(',', '')
    for i in range(20):
        file_1.write(sentence + '\n')
        file_1.write(str(dialog_config.DIALOG_ACT['REQUEST']) + '\n')
    file_2.write(sentence + '\n')
    file_2.write("part_of_day" + '\n')

for sentence in request_event_url:
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "").replace(',', '')
    for i in range(20):
        file_1.write(sentence + '\n')
        file_1.write(str(dialog_config.DIALOG_ACT['REQUEST']) + '\n')
    file_2.write(sentence + '\n')
    file_2.write("event_url" + '\n')

for sentence in request_duration:
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "").replace(',', '')
    for i in range(20):
        file_1.write(sentence + '\n')
        file_1.write(str(dialog_config.DIALOG_ACT['REQUEST']) + '\n')
    file_2.write(sentence + '\n')
    file_2.write("duration" + '\n')

for sentence in greeting:
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "").replace(',', '')
    for i in range(100):
        file_1.write(sentence + '\n')
        file_1.write(str(dialog_config.DIALOG_ACT['GREETING']) + '\n')

for sentence in deny:
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "").replace(',', '')
    for i in range(100):
        file_1.write(sentence + '\n')
        file_1.write(str(dialog_config.DIALOG_ACT['DENY']) + '\n')

for sentence in closing:
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "").replace(',', '')
    for i in range(100):
        file_1.write(sentence + '\n')
        file_1.write(str(dialog_config.DIALOG_ACT['CLOSING']) + '\n')

for sentence in thank:
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "").replace(',', '')
    for i in range(100):
        file_1.write(sentence + '\n')
        file_1.write(str(dialog_config.DIALOG_ACT['THANK']) + '\n')

file_1.close()
file_2.close()