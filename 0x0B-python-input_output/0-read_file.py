#!/usr/bin/python3
'''
The 0-read_file module
'''


def read_file(filename=""):
    '''A function that reads a text file (UTF8) and prints it to stdout'''

    with open(filename, encoding='UTF-8') as a_file:
        '''Opens a file'''
        print(a_file.read(), end='')
