#!/usr/bin/python3
from models.base import Base
"""
Module that creates a Rectangle Class"""


class Rectangle(Base):
    """
    Class Rectangle definition"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiation of a class Rectanle object"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self) -> str:
        """ gets the width"""
        return self.__width

    @property
    def height(self) -> str:
        """ gets the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for the height"""
        self.__height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")  

    @width.setter
    def width(self, width):
        """setter for the width"""
        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
    @property
    def x(self) -> str:
        """ gets the x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for the x"""
        self.__x = x
        if x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self) -> str:
        """ gets the y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for the y"""
        self.__y = y

        if y < 0:
            raise ValueError("y must be >= 0")        

if __name__ == '__main__':
    main()