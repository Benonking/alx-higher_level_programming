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
        area(self)
        display(self)

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

    def area(self):
        """
        Returns area of a rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the rectangle with #
        """
        print("\n" * self.__y + 
                 "\n".join(" " * self.__x + "#" * self.__width 
                     for i in range(self.height)))

    def __str__(self):
        """
        return [Rectangle] (<id>) <x>/<y> - <width>/<height>

        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.__class__.__name__, self.id, self.__x,
                self.__y, self.__width, self.__height)


    def update(self, *args, **kwargs):
        """
        assign arguments to each atrribute
        assign Key/value argument to attributes
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.width = v
                elif k == 2:
                    self.height = v
                elif k == 3:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
    
    def to_dictionary(self):
        """
        Retunrs dictionary representation of Rectangle
        """
        r = {}
        r["id"] = self.id
        r["width"] = self.width
        r["height"] = self.height
        r["x"] = self.x
        r["y"] = self.y
        return r
