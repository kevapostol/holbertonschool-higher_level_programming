#!/usr/bin/python3

from sys import argv
sum = 0

if __name__ == '__main__':
    if len(argv) == 1:
        print(0)
    else:
        for i in range(1, len(argv)):
            sum += int(argv[i])
        print(sum)
