#!/usr/bin/python3
"""
a script that adds all arguments to a Python list,
and then save them to a file
"""
from os import path
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if path.exists('add_item.json'):
    obj_json_file = load_from_json_file('add_item.json')
else:
    obj_json_file = []

for a in range(1, len(argv)):
    obj_json_file.append(argv[a])

save_to_json_file(obj_json_file, 'add_item.json')
