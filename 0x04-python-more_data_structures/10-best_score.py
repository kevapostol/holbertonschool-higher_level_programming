#!/usr/bin/python3
def best_score(a_dictionary):
    '''Returns a key with the biggest integer value.'''

    best = 0

    if a_dictionary is None:
        return None

    for k, v in a_dictionary.items():
        if best < v:
            best = v

    return best
