#!/usr/bin/python3
"""
Module 0-add_integer
Contains one method that adds two numbers
"""


def add_integer(a, b=98):
    """ add two ingers"""
    if not isinstance(a, (int, float)):

        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return a + b
