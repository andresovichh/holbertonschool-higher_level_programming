#!/usr/bin/python3
"""
Module that creates Base class"""


class Base:
    """ Creation of Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ the constructor """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
if __name__ == "__main___":
    main()