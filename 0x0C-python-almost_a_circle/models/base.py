#!/usr/bin/python3
"""
Module base.py
contains class Base

"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the Json string repersentation of list_dictionaries
        Attrributes:
            list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        Atrributes:
            list_objs: list of objects
        """
        objs = []
        if list_objs is not None:
            for ob in list_objs:
                objs.append(cls.to_dictionary(ob))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string reperesantation json_string
        Atrritbutes:
                json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

