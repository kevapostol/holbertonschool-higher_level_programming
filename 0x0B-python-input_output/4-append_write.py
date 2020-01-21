#!/usr/bin/python3
'''
The 4-append_write module
'''


def append_write(filename="", text=""):
    '''
    A function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    '''

    with open(filename, encoding='UTF-8', mode='a') as a_file:
        '''Opens a file'''
        return a_file.write(text)
