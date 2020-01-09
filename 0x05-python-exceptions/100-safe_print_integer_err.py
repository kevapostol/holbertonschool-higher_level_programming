#!/usr/bin/python3
from sys import stderr

def safe_print_integer_err(value):
    try:
        stderr.write("{:d}\n".format(value))
        return True
    except:
        return False
