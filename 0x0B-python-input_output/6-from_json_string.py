#!/usr/bin/python3
'''
The 6-from_json_string module
'''

import json
'''Imports the json module'''


def from_json_string(my_str):
    '''
    A function that function that returns an object
    (Python data structure) represented by a JSON string
    '''
    return json.loads(my_str)
