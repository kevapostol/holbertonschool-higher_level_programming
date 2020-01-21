#!/usr/bin/python3
'''
The 5-to_json_string module
'''

import json
'''Imports the json module'''


def to_json_string(my_obj):
    '''
    A function that returns the JSON representation of an object (string)
    '''
    return json.dumps(my_obj)
