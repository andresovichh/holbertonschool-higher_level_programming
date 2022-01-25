#!/usr/bin/python3
""" A module with a class for Rectangle
"""


class Rectangle:
    """Rectangle  is
    created here"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ starting instance"""
        if not isinstance(width, (int, float)):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        # to count how many instances
        Rectangle.number_of_instances += 1

    def __str__(self):
        a_str = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for k in range(self.__width):
                # if isinstance(self.print_symbol, str):
                #     a_str.append(self.print_symbol)
                # elif isinstance(self.print_symbol, list):
                #     for x in self.print_symbol:
                #         a_str += ' '+ x
                    a_str += str(self.print_symbol)

            if i < (self.__height - 1):
                a_str.append("\n")
        return "".join(a_str)

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

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
