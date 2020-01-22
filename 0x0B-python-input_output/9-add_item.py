#!/usr/bin/python3
'''
The 9-add_item script

A script that adds all arguments to a Python list,
and then save them to a file
'''

import json
from sys import argv
'''Imports the json and argv module'''

if len(argv) is 1:
    with open('add_item.json', mode='a', encoding='utf-8') as a_file:
        a_file.write('[]')

if len(argv) > 1:
    for val_str in range(1, len(argv)):
        with open('add_item.json', mode='r', encoding='utf-8') as a_file:
            obj = json.load(a_file)
            obj.append(argv[val_str])

        with open('add_item.json', mode='w', encoding='utf-8') as a_file:
            json.dump(obj, a_file)
