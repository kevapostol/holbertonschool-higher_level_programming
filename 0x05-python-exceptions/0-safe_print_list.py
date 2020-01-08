#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        if my_list:
            for i in range(x):
                print(my_list[i], end='')
                count += 1
            print()
    except TypeError:
        if my_list:
            print()
            return count
    except IndexError:
        if my_list:
            print()
            return count
