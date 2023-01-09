#!/usr/bin/python3
"""
Module  10-square

contains class Square inherits from Rectangle

"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherits fromRectangle who inherits from BaseGeometry
    methods:
        __init__(self,size)
    """
    def __init__(self, size):
        """
        initialsize class
        Args:
            size(int): private
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
