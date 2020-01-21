#!/usr/bin/python3
'''
The 9-rectangle module
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

    def area(self):
        '''Returns the area of a Rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''Prints width/height of a rectangle'''
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
