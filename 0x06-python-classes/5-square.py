#!/usr/bin/python3
"""
Module 5-square
Defines class Square with private size and public area
can access and ipdate size
can print t0 stdout
"""


class Square:
    """
    Definition of class Square
    Args:
        size (int): size of a side of square
        Functions:
        __init__(self,size)
        size(self)
        self(self, val)
        area(self)
        my_print(self)
    """
    def __init__(self, size=0):
        """
        Initialise Square
        Attributes:
        size (int): default  = 0 if none
        """
        self.size = size

    @property
    def size(self):
        """
        Getter
        Returns: size
        """
        return self.__size

    @size.setter
    def size(self, val):
        """
        Setter
        Set size
        """
        if val < 0:
            raise ValueError("size must be >= 0")
        elif type(val) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = val

    def area(self):
        """
        Calculate area
        """
        return self.__size ** 2

    def my_print(self):
        """
        print square
        """
        if self.__size == 0:
            print()
        else:
            for rows in range(self.__size):
                print("#" * self.size)
