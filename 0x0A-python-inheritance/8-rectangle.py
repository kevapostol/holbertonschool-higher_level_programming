#!/usr/bin/python3
'''
The 8-rectangle module
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    A Rectangle class that inherits BaseGeometry
    '''

    def __init__(self, width, height):
        '''Initializes the Rectangle instance'''
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
