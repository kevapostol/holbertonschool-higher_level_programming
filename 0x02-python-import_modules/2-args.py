#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    if len(argv) > 2:
        print('{:d} arguments:'.format(len(argv) - 1))

        for i in range(1, len(argv)):
            print('{}: {}'.format(i, str(argv[i])))

    elif len(argv) == 2:
        print('1 argument:')
        print('1: {}'.format(str(argv[1])))

    else:
        print('0 argument.')
