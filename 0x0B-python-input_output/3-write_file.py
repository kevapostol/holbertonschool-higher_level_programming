#!/usr/bin/python3
'''
The 2-read_lines module
'''


def write_file(filename="", text=""):
    '''
    A function that writes a string to a text file (UTF8) and returns the
    number of characters written
    '''

    with open(filename, encoding='UTF-8', mode='w') as a_file:
        '''Opens a file'''
        return a_file.write(text)
