#!/usr/bin/python3
'''
The 2-read_lines module
'''


def read_lines(filename="", nb_lines=0):
    '''
    A function that reads n lines of a text file (UTF8) and prints it to
    stdout
    '''
    count = 0

    with open(filename, encoding='UTF-8') as a_file:
        '''Opens a file'''
        for line in a_file:
            if count < nb_lines and nb_lines is not 0:
                print(line, end='')
                count += 1
            elif count is 0:
                print(line, end='')
