#!/usr/bin/python3
import sys

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print('{:d} arguments:'.format(len(sys.argv) - 1))

        for i in range(1, len(sys.argv)):
            print('{}: {}'.format(i, str(sys.argv[i])))

    elif len(sys.argv) == 2:
        print('1 argument:')
        print('1: {}'.format(str(sys.argv[1])))

    else:
        print('0 argument.')
