#!/usr/bin/python3
'''
The Sqare module
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    A Square class inheriting Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initializes the private variables'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Str function'''
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        '''Getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for size'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Update the class Square'''
        if len(args) > 0:
            if len(args) is 1:
                self.id = args[0]
            elif len(args) is 2:
                self.id = args[0]
                self.size = args[1]
            elif len(args) is 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            elif len(args) >= 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            return
        if len(kwargs) > 0:
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']

    def to_dictionary(self):
        '''Returns the dictionary representation of a Rectangle'''
        dic = {}
        dic['id'] = self.id
        dic['size'] = self.width
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
