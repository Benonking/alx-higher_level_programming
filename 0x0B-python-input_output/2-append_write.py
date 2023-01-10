#!/bin/python3
"""
Module 2-append_write
contains a function that appends test to a file
"""


def append_write(filename="", text""):
    """
    appends a string at end of a text file
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
