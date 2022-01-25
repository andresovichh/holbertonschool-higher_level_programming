#!/usr/bin/python3
""" A module with a class for Rectangle
"""


class Rectangle:
    """Rectangle  is
    created here"""

    def __init__(self, width=0, height=0):
        """ starting instance"""
        self.__width = width
        self.__height = height

        if not isinstance(width, (int, float)):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(width, (int, float)):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """ gest the value of`width`"""
        return self.__width
    
    @property
    def height(self):
        """ Gets  the value of `height`"""
        return self.__height

    @width.setter
    def width(self, value):
        """ sets the value of `width`"""
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @height.setter
    def height(self, value):
        """ sets  the value of `height`"""
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

