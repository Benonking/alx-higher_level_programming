#!/usr/bin/python3
"""
Module - 2-is_same_class.py
contains function that checks if object is exactly
an instance of a spefic class
"""


def is_same_class(obj, a_class):
    """checks if an object is an instance of a specific class"""
    if not isinstance(obj, a_class):
        return False
    return True
