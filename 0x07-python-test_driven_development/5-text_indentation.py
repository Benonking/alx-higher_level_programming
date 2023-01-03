#!/usr/bin/python3
"""
Module 5-text_indetation
ptints two new line after each of [".", ",", ":"]
"""


def text_indentation(text):
    """
    """
    if type(text) is not str:
        raise TypeError("text must a string")
    else:
        for char in ".?:":
            text = text.replace(char, char + "\n\n")
        list_lines = [lines.strip(' ') for lines in text.split('\n')]
        rev = "\n".join(list_lines)
        print(rev, end='')
