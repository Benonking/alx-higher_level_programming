#!/usr/bin/python3
"""
Module base.py
contains class Base

"""

class Base:
    """
    Methods:
        __init__
    Attributes:
        nb_objects(private)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialse class
        check if Id is Null or increment nb_ojects
        Args:
            id:(int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
