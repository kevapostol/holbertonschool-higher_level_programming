#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0

    try:
        result = a / b
        print("Inside result: {:d}".format(result))
    except:
        result = None
        print("Inside result: None")
    finally:
        return result
