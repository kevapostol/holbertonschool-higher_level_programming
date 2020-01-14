#!/usr/bin/python3
'''
The 0-rectangle module
'''


class Rectangle:
    '''
    The Rectangle class
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''returns the rectangle area'''
        return self.__width * self.__height

    def perimeter(self):
        '''returns the rectangle perimeter'''
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        '''prints a rectangle'''
        if self.__width is 0 or self.__height is 0:
            return ''

        new_str = ''

        for i in range(self.__height):
            for j in range(self.__width):
                new_str += '#'
            new_str += '\n'
        new_str = new_str[:-1]
        return new_str

    def __repr__(self):
        '''returns a string representation of a rectangle'''
        return '{self.__class__.__name__}({self.width}, {self.height})'.format(
            self=self)

    def __del__(self):
        '''deletes a instance of a class'''
        print('Bye rectangle...')
