#!/usr/bin/python3
"""
Module 1-write_file
contains method to write a string to a file
"""


def write_file(filename="", text=""):
    """
    write a string to file
    Args:
        filename
        text: string to be writen
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
