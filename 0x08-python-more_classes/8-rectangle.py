#!/usr/bin/python3
"""
Module - 8-recatngle.py
Defines class Rectangle
with private attributes width and height
Public attributes number_of_instances,
print_symbol - print rectangle of a certain symbol provided
Defines area a perimeter functions
delete, and keeps tracks of number of instances
Compares two area of two rectangles
"""


class Rectangle:
    """
    Defines class rectangle with private atrributes width and height
    Args:
        width(int): width
        height(height): height

        Attributes:
            number _of_instances
            print_symbol
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
        bigger_or_equal
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialises Rectangle
        Attributes:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter
        Returns width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter
        Args:
            value:sets width to value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns area
        """
        return self.__width * self.__height

    def perimeter(self):
        """"
        Returns perimewter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """prints rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = "\n".join([str(self.print_symbol) * self.__width
                        for rows in range(self.__height)])
        return pic

    def __repr__(self):
        """
        prints string representation of rectangle with #
        """

    def __repr__(self):
        """
        prints string representation of rectangle with #
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes instance of rectangle
        """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
