#!/usr/bin/python3
"""
a foo to multiply two matrices
"""
from typing import Type


def matrix_mul(m_a, m_b):

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for a_list in m_a:
        if not isinstance(a_list, list):
            raise TypeError("m_a must be a list of lists")
    for a_list in m_b:
        if not isinstance(a_list, list):
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for a_list in m_a:
        for item in a_list:
            if not isinstance(item, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for a_list in m_b:
        for item in a_list:
            if not isinstance(item, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    length_a = []
    for a_list in m_a:
        length_a.append(len(a_list))
    first_element = length_a[0]
    for element in length_a:
        if element != first_element:
            raise TypeError("each row of m_a must be of the same size")

    length_b = []
    for b_list in m_b:
        length_b.append(len(b_list))
    first_element = length_b[0]
    for element in length_b:
        if element != first_element:
            raise TypeError("each row of m_b must be of the same size")
    result = [] # final result
    for i in range(len(m_a)):

        row = [] # the new row in new matrix
        for j in range(len(m_b[0])):
        
            product = 0 # the new element in the new row
            for v in range(len(m_a[i])):
                product += m_a[i][v] * m_b[v][j]
            row.append(product) # append sum of product into the new row
        
        result.append(row) # append the new row into the final result
    return result