#!/usr/bin/python3
"""
Module 0-read_file
contains method to read a file
"""


def read_file(filename=""):
    """
    read file and print to STDOUT
    Args:
        filename
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
