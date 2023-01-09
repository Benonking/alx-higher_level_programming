#!/usr/bin/python3
"""
Module - 1-my_list.py
contains method that inherits from list
"""


class MyList(list):
    """
    inherits from list
    functions:
        print_sorted(self)
    """
    def print_sorted(self):
        """
        pritns list in ascending order
        """
        print(sorted(self))
