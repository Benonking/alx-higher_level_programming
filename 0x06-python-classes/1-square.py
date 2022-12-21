#!/usr/bin/python3
"""
Module 1-square
Defines class square with private attribute size

"""


class Square:
    """
    class Square definition
    Args:
        size: size of the side in square
    """
    def __init__(self, size):
        """
        Initializes square
        Attributes:
            size: size of the side of square
        """
        self.__size = size
