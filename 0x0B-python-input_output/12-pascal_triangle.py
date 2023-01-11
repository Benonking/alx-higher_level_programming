#!/usr/bin/python3
"""
Module 12--pascal_triangle
contains a function that impliments list of pascals triangle given size
"""


def pascal_triangle(n):

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    items = [[i]]
    for rows in range(n-1):
        items.append(a+b for a, b in zip([0] + items[-1], items[-1] + [0]))
    return items
