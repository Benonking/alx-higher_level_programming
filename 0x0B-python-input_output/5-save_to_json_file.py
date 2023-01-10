#!/usr/bin/python3
"""
Module 5-save_to_json_file
Contains a function that writes an object to a text file
"""


import json


def save-to_json_file(my_obj, filename):
    """
    save object to file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
