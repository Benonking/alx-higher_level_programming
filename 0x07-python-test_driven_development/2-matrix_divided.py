#!/usr/bin/python3

"""
Module 2-matrix_divided
module contsains one method that takes in a matrix and
returns a matrix whose elements have been divided by div
"""


def matrix_divided(matrix, div):
    """
        Return matrix divided by div to the round of 2
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)
    n_matrix = []
    n_list = []
    samelen = len(matrix[0])

    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(msg)
        if len(lists) != samelen:
            raise TypeError("Each row of the matrix must have the same size")
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)
            n_list.append(round(i/div, 2))
        n_matrix.append(n_list)
    return n_matrix
