#!/usr/bin/python3

"""
An empty class definition"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle"""

    def __init__(self, width, height):
        """ Instance creation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
