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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON rep of a list of dic"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves to a file """

        name = str(cls.__name__) + ".json"
        a_list = []
        with open(name, 'w', encoding='utf8') as f:
            if list_objs is None:
                f.write(cls.to_json_string(a_list))
            else:
                for obj in list_objs:
                    a_list.append(cls.to_dictionary(obj))
                f.write(cls.to_json_string(a_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the string rep
        json_string"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an isntance with all attributes
        already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            dummy = cls(1, 1)
        if cls.__name__ == Square:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        filename = '{}.json'.format(cls.__name__)

        if not filename:
            return []

        with open('{}.json'.format(cls.__name__), 'r+', 'utf-8') as f:
            return 2
