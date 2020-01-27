#!/usr/bin/python3
'''
The Rectangle module
'''
from models.base import Base


class Rectangle(Base):
    '''
    A Rectangle class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes the private variables'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Width setter'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''Height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Height setter'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''X getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''X setter'''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''Y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Y setter'''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''Returns the area value of the Rectangle instance'''
        return self.__width * self.__height

    def display(self):
        '''Prints in stdout the Rectangle instance with the character #'''
        if self.__width is 0 or self.__height is 0:
            return ''

        new_str = ''

        for i in range(self.__y):
            new_str += '\n'
        for i in range(self.__height):
            for j in range(self.__x):
                new_str += ' '
            new_str += '#' * self.__width + '\n'
        print(new_str[:-1])

    def __str__(self):
        '''Str function'''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''Update the class Rectangle'''
        if len(args) > 0:
            if len(args) is 0:
                return
            elif len(args) is 1:
                self.id = args[0]
            elif len(args) is 2:
                self.id = args[0]
                self.width = args[1]
            elif len(args) is 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            elif len(args) is 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            elif len(args) >= 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            return
        if len(kwargs) > 0:
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']

    def to_dictionary(self):
        '''Returns the dictionary representation of a Rectangle'''
        dic = {}
        dic['x'] = self.x
        dic['y'] = self.y
        dic['width'] = self.width
        dic['height'] = self.height
        dic['id'] = self.id
        return dic
