#!/usr/bin/python3
'''
The Base module
'''

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
