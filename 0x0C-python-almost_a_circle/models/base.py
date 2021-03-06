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
        list_t = []

        if list_objs is not None:
            for instance in list_objs:
                list_t.append(cls.to_dictionary(instance))

            list_t = cls.to_json_string(list_t)
        else:
            list_t = '[]'

        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='utf-8') as a_file:
            a_file.write(list_t)

    def from_json_string(json_string):
        '''Returns the list of the JSON string representation json_string'''
        if json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set'''
        dummy_obj = {}

        if cls.__name__ == 'Rectangle':
            dummy_obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_obj = cls(1)

        dummy_obj.update(**dictionary)

        return dummy_obj

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances'''
        try:

            with open(cls.__name__ + '.json', mode='r', encoding='utf-8') as f:
                mylist = f.read()

        except:
            return []

        all_inst = []
        newlist = cls.from_json_string(mylist)

        for i in newlist:
            all_inst.append(cls.create(**i))
        return all_inst
