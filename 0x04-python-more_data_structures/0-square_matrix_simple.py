#!/usr/bin/python3
'''
compute square value of all integers of a matrix
'''
def square_matrix_simple(matrix=[]):
    if matrix != None:
        NewMatrix=[]
        for row in matrix:
            NewMatrix.append(list(map(lambda x: x**2,row)))
        return (NewMatrix)
    return None
