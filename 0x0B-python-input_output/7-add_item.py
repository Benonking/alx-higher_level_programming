#!/usr/bin/python3
"""
Module 7-add_item
Contains script that adds all argu,ents to a python list and then save
them to a file
"""


import sys

save_to_json_file = __import__('5-save_to_jason_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').save_from_json_file

f = add_item.json
try:
    a_list = load_from_json_file(f)
except(TypeError, FileNotFoundError):
    a_list = []

for i in sys.argv[1:]:
    a_list.append(i)
save_to_json_file(a_list, f)
