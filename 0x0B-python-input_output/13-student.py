#!/usr/bin/python3
'''
The 11-student module
'''


class Student:
    '''
    A class Student
    '''

    def __init__(self, first_name, last_name, age):
        '''Initializes a instance'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary representation of a Student instance'''
        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        '''Replaces all attributes of the Student instance'''
        if len(json) is not 0:
            self.first_name = json['first_name']
            self.last_name = json['last_name']
            self.age = json['age']
