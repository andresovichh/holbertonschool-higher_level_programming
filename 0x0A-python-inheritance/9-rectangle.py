#!/usr/bin/python3

"""
An empty class definition"""


BaseGeometry = __import__('8-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle"""

    def __init__(self, width, height):
        """ Instance creation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area method def"""
        return (self.__width * self.__height)

    def __str__(self):
        """ the str method"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
