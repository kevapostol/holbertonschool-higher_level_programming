#!/usr/bin/python3
'''
The 7-save_to_json_file module
'''

import json
'''Imports the json module'''


def save_to_json_file(my_obj, filename):
    '''
    A function that writes an Object to a text file,
    using a JSON representation
    '''
    with open(filename, mode='w', encoding='utf-8') as a_file:
        '''Opens a file'''
        json.dump(my_obj, a_file)
