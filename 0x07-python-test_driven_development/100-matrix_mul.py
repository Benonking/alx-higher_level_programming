#!/usr/bin/pythom3
"""
Module - 100-matrix_mul

"""
def matrix_mul(m_a, m_b):
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if len(m_a) == 0 or len(m_b) == 0 or m_a == [[]] or m_b == [[]]:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    
    for row in m_a:
        for i in row:
            if not isinstance(i, (int,float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        if len(row) != len(m_b[0]):
            raise ValueError("m_a and m_b can't be multiplied")
    
    for row in m_b:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_a must be of the same size")
    n_matrix = []
    i = 0
    lists = []
    for row1 in range(len(m_a)):
        lists = []
        for col1 in range(len(m_b)):
            for element in range(len(m_a[0])):
                i += m_a[row1][element] * m_b[element][col1]
            lists.append(i)
            i = 0
        n_matrix.append(lists)
    return n_matrix




  


