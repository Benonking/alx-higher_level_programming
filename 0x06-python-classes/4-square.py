#!/usr/bin/python3

"""
Module 4-square
Defines class Sqaure with private attribute size and public area
"""


class Square:
    """
    Initialises Square
    Args:
        size (int): size of a side in square
    Funcrions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
    """
    def __init__(self, size=0):
        """
        Initialise class Square
        Attributes:
            size(int): default = 0 if none

        """
        self.size = size

    @property
    def size(self):
        """
        Getter
        Return size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
            value: sets size to value, if int and >=0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size mus be be >=0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate area
        Return:
            area
        """
        return (self.__size) **2
