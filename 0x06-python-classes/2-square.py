#!/usr/bin/python3

""" define a class Square
das
"""


class Square:
    """ this is the Square
    class
    """
    def __init__(self, size=0):
        """ blah blas cajs"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
