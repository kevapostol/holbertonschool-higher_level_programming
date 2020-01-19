#!/usr/bin/python3
'''
The 5-text_indentation module

This module has a funciton that indents text
'''


def text_indentation(text):
    '''
    The function that that prints My name is <first name> <last name>
    '''

    st = ''

    if isinstance(text, str) is False:
        raise TypeError('text must be a string')

    special = {'.', '?', ':'}

    for char in text:

        if char not in special:
            st += char
        else:
            st += char
            print('{}\n'.format(st.strip()))
            st = ''
