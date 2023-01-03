#!/usr/bin/python3
"""
Module 4-print_square
print square given size
"""


def print_square(size):
    """
    print # size of a square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size musr be >=0")
    if type(float) is float and size < 0:
        raise ValueError("size must be an integer")
    else:
        for row in range(size):
            print("#"*size)
