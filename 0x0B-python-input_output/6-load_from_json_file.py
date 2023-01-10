#!/usr/bin/python3
"""
Module 6-load_from_json_file
containd a function that creates an object from a JSON file
"""


def load_from_json_file(filename):
    """
    create an oject fron json file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
