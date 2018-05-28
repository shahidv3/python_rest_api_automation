import csv
import requests
from requests.auth import HTTPBasicAuth
import logging
import nose
import json

global input
global nr

import api_assertions

def get_instance_id(r):
    ''' get id of API instance '''
    global instance_id
    dict_text = json.loads(r.text)
    print dict_text
    result_index = dict_text['result']['accepted']
    instance_id = result_index[0]['id']
    print instance_id
    return instance_id


def api_methods_get(i, instance_id, input):
    ''' get newly created API instance details '''
    r = requests.get(input[i]['url'] + input[i]['resources'] +
                     instance_id, auth=(input[i]['username'], input[i]['apikey']))
    print r.status_code
    api_assertions.assert_status_code(None, r.status_code)


def api_methods_put(i, instance_id, input):
    ''' update newly created API instance  '''
    r = requests.put(input[i]['url'] + input[i]['resources'] +
                     instance_id, data=input[i]['payload'], auth=(input[i]['username'], input[i]['apikey']))
    print r.status_code
    api_assertions.assert_status_code(None, r.status_code)


def api_methods_delete(i, instance_id, input):
    ''' delete newly created API instance  '''
    r = requests.delete(input[i]['url'] + input[i]['resources'] +
                    instance_id, auth=(input[i]['username'], input[i]['apikey']))
    print r.status_code
    api_assertions.assert_status_code(None, r.status_code)


def api_methods_all(input):
    nr = len(input)
    for i in range(nr):
        if input[i]['method'] == 'post':
            ''' create API using post '''
            r = requests.post(input[i]['url'] + input[i]['resources'], data=input[i]
                              ['payload'], auth=(input[i]['username'], input[i]['apikey']))
            print r.status_code
            print r.text
            get_instance_id(r)
            api_assertions.assert_status_code(None, r.status_code)

        if input[i]['method'] == 'get':
            ''' get all instances '''
            r = requests.get(input[i]['url'] + input[i]['resources'],
                             auth=(input[i]['username'], input[i]['apikey']))
            print r.status_code
            api_assertions.assert_status_code(None, r.status_code)

        if input[i]['method'] == 'put':
            api_methods_put(i, instance_id, input)


        if input[i]['method'] == 'delete':
            api_methods_delete(i, instance_id, input)