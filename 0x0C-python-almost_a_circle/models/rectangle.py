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
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        x(self)
        x(self, value)
        y(self)
        y(self, value)

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width mubst be > 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height mubst be > 0")
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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
