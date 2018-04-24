import re
import time
import datetime
import numpy as np
np.random.seed(2018)
import dialog_config
from keras.utils import to_categorical
from keras.preprocessing import sequence
from keras.layers.embeddings import Embedding
from keras.models import Sequential, load_model
from sklearn.metrics import f1_score, accuracy_score
from keras.layers import LSTM, Dense, TimeDistributed, Bidirectional, Dropout

class NL_understanding():
    def __init__(self):
        self.max_length = 30
        self.num_intent = len(dialog_config.DIALOG_ACT)
        self.num_request = len(dialog_config.REQUEST_SLOTS) - 2
        self.get_info(['IOB_training.txt', 'User_intent.txt', 'request_slot_classification.txt'])
        try:
            self.model_intent = load_model('User_intent.h5')
        except:
            self.train_model(mode = [1])
            self.model_intent = load_model('User_intent.h5')
        try:
            self.model_request = load_model('request_slot_classification.h5')
        except:
            self.train_model(mode = [2])
            self.model_request = load_model('request_slot_classification.h5')
        try:
            self.model_IOB = load_model('IOB_training.h5')
        except:
            self.train_model(mode=[3])
            self.model_IOB = load_model('IOB_training.h5')

    def get_info(self, file_names):
        self.X_tokens = set()
        for file_name in file_names:
            file = open(file_name, 'r')
            data = file.read().lower() \
                       .replace('.', '').replace('?', '').replace('!', '').replace(',', '').split('\r\n')[:-1]
            X = [data[i] for i in range(len(data)) if i % 2 == 0]
            y = [data[i] for i in range(len(data)) if i % 2 == 1]
            self.X_tokens.update(set((' '.join(X)).split()))
            if 'intent' in file_name:
                self.intent_to_int = dict((c, i) for i, c in enumerate(sorted(list(set(y)))))
                self.int_to_intent = dict((i, c) for i, c in enumerate(sorted(list(set(y)))))
            elif 'request' in file_name:
                self.request_to_int = dict((c, i) for i, c in enumerate(sorted(list(set(y)))))
                self.int_to_request = dict((i, c) for i, c in enumerate(sorted(list(set(y)))))
            else:
                y_tokens = sorted(list(set((' '.join(y)).split())))
                self.label_to_int = dict((c, i) for i, c in enumerate(y_tokens))
                self.int_to_label = dict((i, c) for i, c in enumerate(y_tokens))
        self.X_tokens = sorted(list(self.X_tokens))
        self.X_tokens.insert(0, 'UNK')
        self.n_vocab = len(self.X_tokens)
        self.word_to_int = dict((c, i) for i, c in enumerate(self.X_tokens))
        self.int_to_word = dict((i, c) for i, c in enumerate(self.X_tokens))


    def get_classification_data(self, file_name):
        # read data from file
        file = open(file_name, 'r')
        data = file.read().lower()\
            .replace('.', '').replace('?', '').replace('!', '').replace(',', '').split('\r\n')[:-1]
        X = [data[i] for i in range(len(data)) if i%2 == 0]
        y = [data[i] for i in range(len(data)) if i%2 == 1]
        # random sample training data
        index = [i for i in range(len(X))]
        np.random.shuffle(index)
        if len(X) > 50000:
            index = index[:50000]
        X = [X[i] for i in index]
        y = [y[i] for i in index]
        # tokenize and pad x
        sentences = [data.split() for data in X]
        X = [[self.word_to_int[word] for word in words] for words in sentences]
        X = sequence.pad_sequences(X, maxlen=self.max_length)
        # change y to categorical
        if 'intent' in file_name:
            y = [self.intent_to_int[label] for label in y]
            n_classes = self.num_intent
        else:
            y = [self.request_to_int[label] for label in y]
            n_classes = self.num_request
        y = to_categorical(y, n_classes)
        return np.asarray(X), np.asarray(y), n_classes


    def get_IOB_data(self, file_name = 'IOB_training.txt'):
        # read data from file
        file = open(file_name, 'r')
        data = file.read().lower() \
                   .replace('.', '').replace('?', '').replace('!', '').replace(',', '').split('\n')[:-1]
        X = [data[i] for i in range(len(data)) if i % 2 == 0]
        y = [data[i] for i in range(len(data)) if i % 2 == 1]
        # random sample training data
        index = [i for i in range(len(X))]
        np.random.shuffle(index)
        if len(X) > 50000:
            index = index[:50000]
        X = [X[i] for i in index]
        y = [y[i] for i in index]
        # tokenize x
        sentences = [data.split() for data in X]
        X = [np.asarray([self.word_to_int[word] for word in words]) for words in sentences]
        # tokenize y
        y_tokens = sorted(list(set((' '.join(y)).split())))
        labels = [data.split() for data in y]
        y = [[self.label_to_int[word] for word in words] for words in labels]
        # other info
        n_classes = len(y_tokens)
        return X[:40000], y[:40000], X[40000:], y[40000:], n_classes


    def build_model(self, n_vocab, n_classes, classification=True):
        model = Sequential()
        if classification:
            model.add(Embedding(n_vocab, 100, input_length=self.max_length))
            model.add(Dropout(0.3))
            model.add(Bidirectional(LSTM(100, return_sequences=False)))
            model.add(Dense(n_classes, activation='softmax'))
        else:
            model.add(Embedding(n_vocab, 100, input_length=None))
            model.add(Dropout(0.3))
            model.add(Bidirectional(LSTM(100, return_sequences=True)))
            model.add(TimeDistributed(Dense(n_classes, activation='softmax')))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.summary()
        return model


    def train_model(self, mode = 1):

        # 1. User intent classification   2. Request slot classification
        if 1 in mode or 2 in mode:
            if 1 in mode and 2 in mode:
                file_names = ['User_intent.txt', 'request_slot_classification.txt']
            elif 1 in mode:
                file_names = ['User_intent.txt']
            elif 2 in mode:
                file_names = ['request_slot_classification.txt']
            for file_name in file_names:
                X_data, y_data, n_classes = self.get_classification_data(file_name)
                if 'intent' in file_name:
                    batch_size = 30
                    epochs = 4
                    validation_split = 0.33
                elif 'request' in file_name:
                    batch_size = 5
                    epochs = 12
                    validation_split = 0.2
                model_classification = self.build_model(self.n_vocab, n_classes)
                model_classification.fit(X_data, y_data, epochs=epochs, batch_size=batch_size,
                                         validation_split=validation_split)
                model_classification.save(file_name.replace('.txt', '.h5'))

        # 3. IOB labeling
        if 3 in mode:
            file_name = 'IOB_training.txt'
            X_IOB, y_IOB, X_test_IOB, y_test_IOB, n_classes_IOB = self.get_IOB_data(file_name)
            model_IOB = self.build_model(self.n_vocab, n_classes_IOB, classification=False)
            for iteration in range(10):
                print('-------------- training iteration {} ---------------'.format(iteration))
                for i in range(len(X_IOB)):
                    model_IOB.train_on_batch(np.asarray(X_IOB[i])[np.newaxis, :],
                                             np.eye(n_classes_IOB)[y_IOB[i]][np.newaxis, :])
                model_IOB.save(file_name.replace('.txt', '.h5'))

            y_pred = []
            for i in range(len(X_test_IOB)):
                y_pred.append(np.argmax(model_IOB.predict_on_batch(X_test_IOB[i][np.newaxis, :]), -1)[0])

            accuracy = np.mean([accuracy_score(y_test_IOB[i], y_pred[i]) for i in range(len(y_test_IOB))])
            f1 = np.mean([f1_score(y_test_IOB[i], y_pred[i], average='weighted') for i in range(len(y_test_IOB))])
            print('Test Accuracy: {} \nTest F1: {}'.format(accuracy, f1))

            # show example
            sample_indices = np.random.randint(0, len(y_IOB), size=10)
            sample_texts = [X_IOB[i] for i in sample_indices]
            sample_labels = [y_IOB[i] for i in sample_indices]

            pred_labels = [np.argmax(model_IOB.predict(sample_texts[i][np.newaxis, :]), -1)[0] for i in
                           range(len(sample_indices))]
            for i in range(len(sample_indices)):
                sentence = [self.int_to_word[j] for j in sample_texts[i]]
                real_label = [self.int_to_label[j] for j in sample_labels[i]]
                pred_label = [self.int_to_label[j] for j in pred_labels[i]]
                print('Sentence: {} \nReal: {} \nPredict: {} \n'.format(sentence, real_label, pred_label))


    def guess_date(self, value):
        dict_weekdays = {'monday':0, 'tuesday': 1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6,
                'mon':0, 'tue':1, 'tues':1, 'wed':2, 'weds':2, 'thu':3, 'thurs':3, 'fri':4, 'sat':5, 'sun':6}
        dict_months = {'january':'jan', 'february':'feb', 'march':'mar', 'april':'apr', 'may':'may', 'june':'jun',
                       'july':'jul', 'august':'aug', 'september':'sep', 'october':'oct', 'november':'nov',
                       'december':'dec', 'sept':'sep'}
        today = datetime.datetime.now()
        for i in value.split(' '):
            if i in dict_weekdays.keys():
                day_of_week = today.weekday()
                delta = 7 - day_of_week + dict_weekdays[i]
                value = today + datetime.timedelta(days=delta)
                value = value.strftime('%m/%d/%Y')
            elif i in dict_months:
                value.replace(i, dict_months[i])
        if 'next month' in value:
            year = str(today.year)
            month = str(today.month + 1)
            day = '01'
            value = '{}/{}/{}'.format(month, day, year)
        for fmt in ["%m/%d/%Y", "%Y/%m/%d", "%d-%m-%Y", "%m/%d", "%Y/%m", "%m/%Y"
                    "%Y%m%d", "%Y%m", "%m%d", "%Y %m %d", "%Y %m", "%m %d",
                    "%d %b %Y", "%d %b", "%b %Y", "%Y %b", "%Y %b %d"]:
            try:
                date = time.strptime(value, fmt)
                return date
            except:
                continue
        return None


    def convert_nl_to_state(self, response_action):
        sentence = response_action['sentence'].replace('?', '').replace('!', '').replace(',', ''). replace('.', '').lower()
        x = []
        for word in list(filter(None, sentence.split(' '))):
            if word in self.X_tokens:
                x.append(self.word_to_int[word])
            else:
                x.append(self.word_to_int['UNK'])
        x = np.asarray(x)[np.newaxis, :]
        x_classification = sequence.pad_sequences(x, maxlen=self.max_length)
        pred_intent = np.argmax(self.model_intent.predict(x_classification))
        intent = self.int_to_intent[pred_intent]
        response_action['act'] = int(intent)

        if intent == '0':
            pred_request = np.argmax(self.model_request.predict(np.asarray(x_classification)))
            request = self.int_to_request[pred_request]
            response_action['request_slots'] = [request]
        elif intent == '1':
            pred_label = np.argmax(self.model_IOB.predict(x), -1)[0]
            label = [self.int_to_label[i] for i in pred_label]
            words = sentence.split(' ')
            print(words)
            print(label)
            for slot in dialog_config.INFORMATION_SLOTS:
                if 'b-' + slot in label or 'i-' + slot in label:
                    indices = [i for i in range(len(label)) if label[i] == 'b-' + slot or label[i] == 'i-' + slot]
                    value = ' '.join([words[i] for i in indices])

                    if slot == 'date_start':
                        date = self.guess_date(value)
                        if date is None:
                            continue
                        value = time.strftime('%m/%d/%Y', date)
                    if slot == 'time':
                        value = re.sub("[^0-9]", "", value)
                        if len(value) < 4:
                            for _ in (4 - len(value)):
                                value += '0'
                        elif len(value) > 4:
                            value = value[:4]
                        if 'pm' in value:
                            value = str(int(value) + 1200)
                        value = value[:2] + ':' + value[2:]
                    if slot == 'price':
                        value = re.sub("[^0-9]", "", value)
                    if slot == 'is_weekend':
                        if value in ['weekend', 'sat', 'saturday', 'sun', 'sunday']:
                            value == 'weekend'
                        else:
                            value == 'weekday'
                    if slot == 'part_of_day':
                        if value in ["morning", "sunrise", "sun rise", "daytime", "day light", "dawn"]:
                            value == 'morning'
                        elif value in ["afternoon", "noon", "mid day", "midday"]:
                            value == 'afternoon'
                        else:
                            value == 'evening'
                    response_action['inform_slots'][slot] = value
        return response_action


if __name__ == '__main__':
    nlu = NL_understanding()
    while True:
        action = {}
        action['act'] = -1
        action['inform_slots'] = {}
        action['request_slots'] = []
        action['turn'] = 0
        action['sentence'] = raw_input("User input: ")
        nlu.convert_nl_to_state(action)
        print(action)