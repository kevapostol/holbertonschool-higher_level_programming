#!/usr/bin/python3
'''
The 3-is_kind_of_class module
'''


def is_kind_of_class(obj, a_class):
    '''
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class ; otherwise
    False
    '''
    if issubclass(type(obj), a_class):
        return True
    return False
