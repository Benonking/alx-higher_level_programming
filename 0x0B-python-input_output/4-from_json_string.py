#!/usr/bin/python3
"""
Module - 4-from_json_string
Contains a method that returns an oject represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    returns an oject represented by a json string
    """
    return json.loads(my_str)
