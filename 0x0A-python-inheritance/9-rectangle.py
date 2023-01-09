#!/usr/bin/python3
"""
Module 9-rectangle
contains clas Rectangle that inherits from BaseGeometry
contains area() implimetation

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    methods:
        __init__(self, width, height)
        area(self)
        __str__(self)
    """
    def __init__(self, width, height):
        """
        Args:
            width(int): private
            height(int): private
        """
        self.__height = height
        self.__width = width

        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """
        extent parent method and returns area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        print out output
        """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
