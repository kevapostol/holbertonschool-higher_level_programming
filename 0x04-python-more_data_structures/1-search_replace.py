#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    new_list = [(replace if ele == search else ele) for ele in new_list]
    return(new_list)
