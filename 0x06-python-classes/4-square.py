#!/usr/bin/pytthon3

"""
Module 4-square
Defines class Sqaure with private attribute size
"""


class Square:
    """
    Initialises Sqaure
    Args:
        size (int): size of a side in sqaure
    Funcrions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
    """
    def __int__(self, size=0):
        """
        Initialise class Square
        Attributes:
            sie(int): default = 0 if none

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
            raise ValueError("size musbe be >=0")
        else:
            self.__size = value

    def area(self):
        """
        Calulate area
        Return:
            area
        """
        return (self.__size) **2
