#!/usr/bin/python3
"""
Module that creates a class"""


class Student:
    """
    a class student"""
    def __init__(self, first_name, last_name, age):
        """ instanciation od class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary """
        a = {}
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list):
            for strings in attrs:
                if strings in self.__dict__:
                    a[strings] = self.__dict__[strings]
            return a
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the
        Studen instance"""
        for x in json.items():
            self.__dict__.update(x)
