#!/usr/bin/python3
"""
Module Rectangle
contains class Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    initilase class rectanggle
    Methods:
        __init__(self, width, height, x=0, y=0, id=None)

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """
        Getter
        Return self.width
        """
        return self.__width
    @width.setter
    def width(self, value):
        """
        Setter
        sets self.__width to value
        Args:
            value
        """
        self.__width = value
    
    @property
    def height(self):
        """
        Getter
        Return self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter
        sets self.__height to value
        Args:
            value
        """
        self.__height = value
    
    @property
    def x(self):
        """
        Getter
        Return self.__x
        """
        return self.__x
    
    @x.setter
    def x(self, value):
        """
        Setter
        sets self.__x to value
        Args:
            value
        """
        self.__x = value
    
    @property
    def y(self):
        """
        Getter
        Return self.__y
        """
        return self.__y
    
    @y.setter
    def y(self, value):
        """
        Setter
        sets self.__y to value
        Args:
            value
        """
        self.__y = value
