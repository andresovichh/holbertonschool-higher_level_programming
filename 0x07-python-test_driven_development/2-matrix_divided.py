#!/usr/bin/python3

def matrix_divided(matrix, div):
    # if  not isinstance(matrix, list):#check if mtrix of lists
    #     raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # for x in matrix:
    #     if
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for list_ in matrix:#check if all lists are same size
        list_of_lengths = []
        for list_ in matrix:
            list_of_lengths.append(len(list_))
    #print(list_of_lengths)
    if not (list_of_lengths.count(list_of_lengths[0]) == len(list_of_lengths)):
        raise TypeError("Each row of the matrix must have the same size")
    for list_ in matrix:
        if not isinstance(list_, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for element in list_:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            #print(element)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    for list_ in matrix:
        for element in list_:
            div_result = (element / div)
            rnd_result = round(div_result, 2)
            new_list.append(rnd_result)
    return new_list  

