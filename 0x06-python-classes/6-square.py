#!/usr/bin/python3
"""
Module 5-square
Defines class Square with private size and public area
can access and ipdate size
can print to stdout
"""


class Square:
    """
    Definition of class Square
    Args:
        size (int): size of a side of square
        Functions:
        __init__(self,size)
        size(self)
        position(self)
        position(self, value)
        self(self, val)
        area(self)
        my_print(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise Square
        Attributes:
        size (int): default  = 0 if none
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter: Returns position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets position
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))
