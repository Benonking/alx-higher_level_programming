#!/usr/bin/python3
"""
Module 7-base_geometry
contains class BaseGeometry, instance area(), instance integer_validator()
"""


class BaseGeometry:
    """
    methods:
        area()
        integer_validator()
    """
    def area(self):
        """
        raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate input
        Args:
            name(str): string
            value(int): >0
        """
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
