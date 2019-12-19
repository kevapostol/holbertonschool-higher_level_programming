#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''Adds all unique integers in a list (only once for each integer).'''

    new_list = my_list[:]
    new_list = [(replace if ele == search else ele) for ele in new_list]
    return(new_list)
