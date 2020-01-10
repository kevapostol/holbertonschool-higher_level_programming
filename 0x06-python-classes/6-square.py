#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is False or isinstance(value[0], int) is\
            False or isinstance(value[1], int) is False or value[0] < 0 or\
                value[1] < 0:
            raise ValueError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for m in range(self.__position[0]):
                    print(' ', end='')

                for j in range(self.__size):
                    print('#', end='')
                print()

    def area(self):
        return self.__size ** 2
