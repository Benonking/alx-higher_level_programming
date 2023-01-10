#!/usr/bin/python3
"""
Module - 3-to_json_string
Contains a method that returns a JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """
    return Json repsentation
    """
    return json.dumps(my_obj)
