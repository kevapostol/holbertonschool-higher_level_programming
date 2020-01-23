#!/usr/bin/python3
'''
The 10-class_to_json module
'''

import json
'''Imports the json and argv module'''

def class_to_json(obj):
    '''
    function that returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of
    an object
    '''
    return obj.__dict__
