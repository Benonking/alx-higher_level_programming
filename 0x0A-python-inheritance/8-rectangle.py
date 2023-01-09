#!/usr/bin/python3
"""
Module 8-rectangle
contains sub class Rectangle that inherits BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    inherits class BaseGeometry
    Methods
        __init__(self,width,height)

    """
    def __init__(self, width, height):
        """
        Args:
            width(int) - private
            height(int) - private
        """
        self.__width = width
        self.__height = height

        super().integer_validator("width", width)
        #self.__width = width
        super().integer_validator("height", height)
        #self.__height = height
