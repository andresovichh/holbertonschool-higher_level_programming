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

    def area(self):
        """ Area definition s"""
        return (self.__width * self.__height)

    def __str__(self):
        """ string method"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


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
