#!/usr/bin/python3
"""
Module 9-student
contains class student
"""


class Student:
    """
    class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Inititialsie class  Student
        Args:
            first_name: public
            last_name: public
            age: public
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, objs):
        """
        Returns a dictionary discription of a simple data structure
        for JSON seriallization of an object
        Args:
        obj: python object

        """
        if objs is None:
            return self.__dict__
        else:
            dic = {}
            for obj in objs:
                if obj in self.__dict__.keys():
                    dic[obj] = self.__dict__[obj]
            return dic
