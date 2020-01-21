#!/usr/bin/python3
'''
The 7-base_geometry module
'''


class BaseGeometry:
    '''
    A BaseGeometry class
    '''

    def area(self):
        '''Raises an exception area is not implemented.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates the value.'''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
