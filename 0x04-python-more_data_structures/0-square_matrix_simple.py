#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = []
    for row in matrix:
        my_matrix.append([x ** 2 for x in row])
    return my_matrix
