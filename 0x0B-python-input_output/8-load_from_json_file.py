#!/usr/bin/python3
'''
The 8-load_from_json_file module
'''

import json
'''Imports the json module'''


def load_from_json_file(filename):
    '''
    A function that creates an Object from a “JSON file"
    '''
    with open(filename, mode='r', encoding='utf-8') as a_file:
        '''Opens a file'''
        return json.load(a_file)
