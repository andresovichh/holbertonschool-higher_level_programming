#!/usr/bin/python3
"""
Module that creates a Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle definition"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiation of a class Rectanle object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ gets the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter for the width"""
        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """ gets the height"""
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """ gets the x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for the x"""
        self.__x = x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self) -> str:
        """ gets the y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for the y"""
        self.__y = y

        if type(y) is not int:
            raise TypeError("y must be an integer")

        elif y < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """ REturns area of Rectangle"""
        return self.width * self.height

    def display(self):
        """ prints a rectangle pattern"""
        if self.y <= 0:
            pass
        else:
            print("\n"*int(self.y - 1))
        for a in range(self.height):
            print(" " * self.x, end="")
            for b in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ override str"""
        return '[Rectangle] ('+str(self.id)+') '+str(self.x)+'/'+str(self.y) +\
            ' - '+str(self.width)+'/'+str(self.height)

    def update(self, *args, **kwargs):
        """ update the data"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            for key, value in kwargs.items():
                # if key == "id":
                #     self.id = value["id"]
                # if key == "width":
                #     self.width = value["width"]
                # if key == "height":
                #     self.height = value["height"]
                # if key == "x":
                #     self.x = value["x"]
                # if key == "5":
                #     self.y = value["5"]
                # Setattr(obect, key, value)
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of
        a rectangle"""
        return {"x": self.x,
                "width": self.width,
                "id": self.id,
                "height": self.height,
                "y": self.y,
                }

if __name__ == '__main__':
    main()
