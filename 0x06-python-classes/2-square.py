#!/usr/bin/python3
"""
Module 2-square
Defines class square with private attribute size

"""


class Square:
    """
    class Square definition
    Args:
        size: size of the side in square
    """
    def __init__(self, size=0):
        """
        Initializes square
        Attributes:
            __size: size of the side of square
        """
        if type(size) is not int:
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
