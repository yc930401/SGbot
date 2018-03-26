import re
import time
import datetime
from elasticsearch import Elasticsearch
import dialog_config

def get_training_data(data_size = 1000):
    es = Elasticsearch("http://10.0.109.44:9200/")
    results = es.search(index="sg_meetup_event", body=
    {"query": {
        "bool": {
            "must": [{"term": {"venue.country": "sg"}},
                     {"term": {"status": "upcoming"}}],
            "must_not": [],
            "should": []
        }
    },
        "from": 0,
        "size": data_size,
        "sort": [{"time": {"order": "desc", "mode": "avg"}}]
    })
    return process_data(results)

'''
def search(query_string):
    es = Elasticsearch("http://10.0.109.44:9200/")
    results = es.search(index="sg_meetup_event", body={
                           "query":{
                              "query_string":{
                                "query":query_string
                              }
                           },
                            "size": 5,
                        })
    return process_data(results)
'''

def search(user_informed_slots):
    #should = ["name", "venue_name", "event_host", "date_start", "time", "price"]
    #after = ["is_weekend", "part_of_day", "region"]
    should_query = {}
    string_query = {}
    range_query = {}
    after_query = {}
    for key, value in user_informed_slots.items():
        if key == "name":
            string_query["name"] = re.sub("[^a-zA-Z]","", value)
        elif key == "venue_name":
            string_query["venue.name"] = re.sub("[^a-zA-Z]","", value)
        elif key == "event_host":
            string_query["group.name"] = re.sub("[^a-zA-Z]","", value)
        elif key == "date_start":
            if value != dialog_config.SPECIAL_SLOT_VALUES["I_DO_NOT_CARE"] and \
                    value != dialog_config.SPECIAL_SLOT_VALUES["I_DO_NOT_KNOW"]:
                time_string = value
                querytime = time.strptime(time_string, '%m/%d/%Y')
                if "time" in user_informed_slots.keys():
                    if user_informed_slots["time"] != dialog_config.SPECIAL_SLOT_VALUES["I_DO_NOT_CARE"] and \
                            user_informed_slots["time"] != dialog_config.SPECIAL_SLOT_VALUES["I_DO_NOT_KNOW"]:
                        time_string = value + ' ' + user_informed_slots["time"]
                        querytime = time.strptime(time_string, '%m/%d/%Y %H:%M')
                should_query['time'] = str(time.strftime('%s', querytime)) + '000'
        elif key == "time" and "time" not in should_query.keys():
            if value != dialog_config.SPECIAL_SLOT_VALUES["I_DO_NOT_CARE"] and \
                    value != dialog_config.SPECIAL_SLOT_VALUES["I_DO_NOT_KNOW"]:
                tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
                yes_time_nyr = tomorrow.strftime('%m/%d/%Y')
                time_string = yes_time_nyr + ' ' + value
                querytime = time.strptime(time_string, '%m/%d/%Y %H:%M')
                should_query['time'] = str(time.strftime('%s', querytime)) + '000'
        elif key == "price":
            if value != dialog_config.SPECIAL_SLOT_VALUES["I_DO_NOT_CARE"] and \
                    value != dialog_config.SPECIAL_SLOT_VALUES["I_DO_NOT_KNOW"]:
                range_query['fee.amount'] = float(value.split()[0])
                if len(value.split()) > 1:
                    should_query['fee.currency'] = value.split()[1]
        elif key == "is_weekend":
            after_query["is_weekend"] = value
        elif key == "part_of_day":
            after_query["part_of_day"] = value
        elif key == "region":
            after_query["region"] = value
    print(should_query)
    es = Elasticsearch("http://10.0.109.44:9200/")
    results = es.search(index="sg_meetup_event", body=
    {"query": {
        "bool": {
            "must": [{"term": {"venue.country": "sg"}},
                     {"term": {"status": "upcoming"}},
                     {"range": {
                            "time": {
                                    "gt": ''.join(str(time.time()).split('.')),
                                    "lt": "9999999999000"
                                    }}}],
            "must_not": [],
            "should": [{"match_phrase": {key: value}}
                       for key, value in should_query.items()]+
                        [{"range": {
                            key: {
                                    "gt": value - value/5,
                                    "lt": value + value/5
                                    }}} for key, value in range_query.items()]+
                        [{"query_string": {
                             "default_field": key,
                             "query": value}} for key, value in string_query.items()]
                }
        },
        "from": 0,
        "size": 10,
        "sort": [{"time": {"order": "asc", "mode": "avg"}}]
    })

    return process_data(results, after_query)



def process_data(results, after_query=None):
    if 'hits' in results and 'total' in results['hits']:
        all_data = []
        for event in results['hits']['hits']:
            dict = {}
            score = event['_score']
            dict['_score'] = score
            data = event['_source']
            # get data
            if 'venue' in data.keys():
                if 'localized_country_name' in data['venue'].keys():
                    country = data['venue']['localized_country_name']
                    dict['country'] = country
                if 'address_1' in data['venue'].keys():
                    address = data['venue']['address_1']
                    dict['address'] = address
                if 'city' in data['venue'].keys():
                    city = data['venue']['city']
                    dict['city'] = city
                if 'name' in data['venue'].keys():
                    venue_name = data['venue']['name']
                    dict['venue_name'] = venue_name
                    for item in dialog_config.CENTRAL:
                        if item in venue_name:
                            dict['region'] = 'central'
                            break
                    for item in dialog_config.EAST:
                        if item in venue_name:
                            dict['region'] = 'east'
                            break
                    for item in dialog_config.NORTH:
                        if item in venue_name:
                            dict['region'] = 'north'
                            break
                    for item in dialog_config.NORTH_EAST:
                        if item in venue_name:
                            dict['region'] = 'north east'
                            break
                    for item in dialog_config.WEST:
                        if item in venue_name:
                            dict['region'] = 'west'
                            break
                    dict['region'] = 'other'
            if 'event_url' in data.keys():
                event_url = data['event_url']
                dict['event_url'] = event_url
            if 'duration' in data.keys():
                duration = int(data['duration'])/(60*60*1000)
                dict['duration'] = duration
            if 'name' in data.keys():
                name = data['name']
                dict['name'] = name
            if 'group' in data.keys():
                if 'name' in data['group'].keys():
                    group_name = data['group']['name']
                    dict['event_host'] = group_name
            if 'time' in data.keys():
                date_created = time.strftime("%m/%d/%Y %H:%M %a", time.localtime(int(data['time']/1000)))
                dict['date_start'] = date_created.split()[0]
                dict['time'] = date_created.split()[1]
                hour = dict['time'].split(':')[0]
                if hour >= 6 and hour < 12:
                    dict['part_of_day'] = 'morning'
                elif hour >= 12 and hour < 19:
                    dict['part_of_day'] = 'afternoon'
                else:
                    dict['part_of_day'] = 'evening'
                weekday = date_created.split()[2]
                if weekday == 'Sat' or weekday == 'Sun':
                    dict['is_weekend'] = True
                else:
                    dict['is_weekend'] = False
            if 'fee' in data.keys():
                if 'amount' in data['fee'].keys():
                    amount = data['fee']['amount']
                    if 'currency' in data['fee'].keys():
                        currency = data['fee']['currency']
                        amount = str(amount) + ' '
                    else:
                        currency = ''
                    dict['price'] = str(amount) + currency
                '''
                if 'accept' in data['fee'].keys():
                    accept = data['fee']['accept']
                    dict['pay_by'] = accept            
            if 'rsvp_limit' in data.keys():
                rsvp_limit = data['rsvp_limit']
                dict['rsvp_limit'] = rsvp_limit
            if 'visibility' in data.keys():
                visibility = data['visibility']
                dict['visibility'] = visibility
            '''
            if after_query is not None:
                check = [0 if value == dict[key] else 1 for key, value in after_query.items()]
                if sum(check) == 0:
                    all_data.append(dict)
            else:
                all_data.append(dict)
        return all_data
