#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0

        if my_list:
            for i in range(x):
                print(my_list[i], end='')
                count += 1
            print()
    except IndexError:
        print()
        return count
    finally:
        return count
