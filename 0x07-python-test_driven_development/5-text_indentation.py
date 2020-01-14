#!/usr/bin/python3
'''
The 5-text_indentation module

This module has a funciton that indents text
'''


def text_indentation(text):
    '''
    The function that that prints My name is <first name> <last name>
    '''
    msg = text

    if isinstance(msg, str) is False:
        raise TypeError('text must be a string')

    special = {'.', '?', ':'}
    flag = False

    for c in range(len(msg)):
        if c + 1 < len(msg) and msg[c] in special and msg[c + 1] == ' ':
            print('{}'.format(msg[c]), end='\n\n')
            flag = True
        elif c + 1 < len(msg) and msg[c] in special and msg[c + 1] != ' ':
            print('{}'.format(msg[c]), end='\n\n')
        else:
            if flag is True:
                flag = False
            else:
                print('{}'.format(msg[c]), end='')
