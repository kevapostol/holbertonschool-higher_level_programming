#!/usr/bin/python3
'''
The 5-base_geometry module
'''


class BaseGeometry:
    '''
    class BaseGeometry
    '''
    def area(self):
        '''Raises an exception area is not implemented.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates the value.'''
        if isinstance(value, int) is False:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
