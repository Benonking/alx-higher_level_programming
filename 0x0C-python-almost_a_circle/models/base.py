#!/usr/bin/python3
"""
Module base.py
contains class Base

"""


import json
import csv


class Base:
    """
    Methods:
        __init__
        to_json_string
        save_to-file
        from_json_string
        create
        load_from_file
        save_to_file_csv

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

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all atrributes already set
        Atrrinbutes:
            cls: class
            **dictionary: double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of istances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                listd = cls.from_json_string(file.read())
                return [cls.create(**i) for i in listd]
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        sereilasie and deserializes in CSV
        """
        filename = cls.__name__ + ".csv"
        objs = []
        with open(filename, "w", newline='') as f:
            writer = csv.writer(f)
            for ob in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([ob.id, ob.width, ob.height, ob.x, ob.y])
                if cls.__name__ == "Sqaure":
                    writer.writerow([ob.id, ob.size, ob.x, ob.y])
    
    @classmethod
    def load_from_file_csv(cls):
        """

        """
        objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, "r", newline='') as f:
            file_contents = csv.reader(f)
            for row in file_contents:
                if cls.__name__ == "Rectangle":
                    dic = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                            }
                if cls.__name__ == "Square":
                    dic = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                            }
                ob = cls.create(**dic)
                objs.append(ob)
        return objs
