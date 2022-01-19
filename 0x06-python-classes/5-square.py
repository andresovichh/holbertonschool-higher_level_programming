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

    @property
    def size(self):
        """ Tghis whould be the getter"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """ this would be the setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """REturn area"""
        return self.__size * self.__size

    def my_print(self):
        """ prints a square"""
        if self.__size == 0:
            print("\n", end="")
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print()
