#!/usr/bin/python3
"""
Module - 1-recatngle.py
Defines class Rectangle with private attributes width and height
"""


class Rectangle:
    """
    Defines class rectangle with private atrributes width and height
    Args:
        width(int):width
        height(height): height
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """
        Initialises Rectangle
        Attributes:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter
        return width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter
        Args:
            value:sets width to value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter
        return height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter
        Args:
            value:sets height to value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value
