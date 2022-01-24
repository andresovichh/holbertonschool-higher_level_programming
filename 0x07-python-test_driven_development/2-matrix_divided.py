#!/usr/bin/python3
"""
This module adds integers, with one foo, add_integer()
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """ Returns a matrix divided by div.
    matrix: a matrix
    div: a divisor
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
    for list_ in matrix:  # check if all lists are same size
        list_of_lengths = []
        for list_ in matrix:
            list_of_lengths.append(len(list_))
    if not (list_of_lengths.count(list_of_lengths[0]) == len(list_of_lengths)):
        raise TypeError("Each row of the matrix must have the same size")
    for list_ in matrix:
        if not isinstance(list_, list):
            raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")
        for element in list_:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix \
                    (list of lists) of integers/floats")
            # print(element)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    new_list = [[round((x / div), 2) for x in list_] for list_ in matrix]
    return new_list
