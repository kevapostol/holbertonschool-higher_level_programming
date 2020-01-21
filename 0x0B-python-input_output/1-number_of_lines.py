#!/usr/bin/python3
'''
The 1-number_of_lines module
'''


def number_of_lines(filename=""):
    '''A function that returns the number of lines of a text file'''

    count = 0

    with open(filename, encoding='UTF-8') as a_file:
        '''Opens a file'''
        for line in a_file:
            count += 1

    return count
