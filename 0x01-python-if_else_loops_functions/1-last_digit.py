#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10

if number < 0:
    number *= -1
    last = number % 10
    last *= -1

print("last digit of {:d}".format(number) + " is {:d}".format(last), end=" ")

if last > 5:
    print("and is greater than 5")
elif last == 0:
    print("and is 0")
elif last < 6 and not 0:
    print("and is less than 6 and not 0")
