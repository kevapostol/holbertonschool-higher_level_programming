#!/usr/bin/python3
def no_c(my_string):
    '''Removes all characters c and C from a string.'''

    new_string = ''

    for i in my_string:
        if i is not 'C' and i is not 'c':
            new_string += i
    return (new_string)
