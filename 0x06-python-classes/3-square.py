#!/usr/bin/python3
"""
Module 3-square
Defines a square
"""


class Square:
    """
    Initialises class Sqaure
    Attributes:
       __size: size of side of square
    """

    def __init__(self, size=0):
        if size is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    def area(self):
        """
        calcualte the are of square
        """
        return size * size
