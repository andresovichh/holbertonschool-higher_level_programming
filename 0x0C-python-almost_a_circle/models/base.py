#!/usr/bin/python3
import json
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

    def to_json_string(list_dictionaries):
        """ returns JSON rep of a list of dic"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(sorted(list_dictionaries))
if __name__ == "__main___":
    main()
