#!/usr/bin/python3
'''
The 11-square module
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    A Square class that inherits Rectangle
    '''

    def __init__(self, size):
        '''Initializes an instance'''
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        '''Returns the area of a Square'''
        return self.__size * self.__size

    def __str__(self):
        '''Returns a string when we try to use the print function'''
        return '[Square] {}/{}'.format(self.__width, self.__height)
