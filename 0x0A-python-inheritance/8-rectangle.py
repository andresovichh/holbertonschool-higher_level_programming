#!/usr/bin/python3

"""
An empty class definition"""


class BaseGeometry:
    """
    An empty class"""
    def area(self):
        """ area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ int validator method"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Class Rectangle"""

    def __init__(self, width, height):
        """ Instance creation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
