#!/usr/bin/python3
"""
Module 4-inherits_from

check if object instance was inherited from a class
"""


def inherits_from(obj, a_class):
    """
    check if an instance of an object of a class that
    inherited from a spefied class
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
