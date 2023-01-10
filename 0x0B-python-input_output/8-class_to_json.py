#!/usr/bin/python3
"""
Module 8-class_to_json
containd a funtion that returns a dictionary
description with simpple data structure
"""


def class_to_json(obj):
    """
    Returns a dictionary discription of a simple data structure
    for JSON seriallization of an object
    Args:
        obj: python object
    """
    return obj.__dict__

