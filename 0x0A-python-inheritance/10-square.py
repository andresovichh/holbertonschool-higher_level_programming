#!/usr/bin/python3

"""
An empty class definition"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class square, that inherits from Rectangle"""

    def __init__(self, size):
        """ a square initialization"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area method"""
        return (self.__size * self.__size)

    def __str__(self):
        """ the str method"""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
