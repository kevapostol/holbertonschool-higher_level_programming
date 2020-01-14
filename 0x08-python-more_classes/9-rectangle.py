#!/usr/bin/python3
'''
The 0-rectangle module
'''


class Rectangle:
    '''
    The Rectangle class
    '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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
            new_str += str(self.print_symbol) * self.__width + '\n'
        return new_str[:-1]

    def __repr__(self):
        '''returns a string representation of a rectangle'''
        return '{self.__class__.__name__}({self.width}, {self.height})'.format(
            self=self)

    def __del__(self):
        '''deletes a instance of a class'''
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''static method for returning the biggest rectangle'''
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''class method for creating a new rectangle instance'''
        return cls(size, size)
