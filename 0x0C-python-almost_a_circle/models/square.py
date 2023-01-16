#!/usr/bin/python3
"""
Module- square
Contains class sqaure that inherits from rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square
    Inherited attributes:
        id, __height, __x, __y, __width
    Methods:
        __init__(self, size, x=0, y=0, id=None)
        size(self)
        size(self, value)
        __str__(self)

    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initalise class with inherited atrributes
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        getter
        Return self.size
        """
        return self.width
    
    @size.setter
    def size(self, value):
        """
        seeter size
        sets width and height as
        """
        self.width = value
        self.height = value
    
    def __str__(self):
        """
        return [Square] (<id>) <x>/<y> - <size>

        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(self.__class__.__name__,
                self.id, self.x, self.y, self.size)
    
    def update(self, *args, **kwargs):
        """
        Assignes attributes to argumets if args exist
        if no args given: set attributes according to k/v

        Atrributes
            *args:list of arguments
            **kwargs: double poitet to a dictionary
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

