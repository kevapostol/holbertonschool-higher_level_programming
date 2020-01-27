#!/usr/bin/python3
'''
The Base module
'''
import json


class Base:
    '''
    A Base class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initializes the private variables'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file'''
        print(list_objs.to_dictionary)
