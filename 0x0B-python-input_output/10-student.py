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
                if not isinstance(strings, str):
                    return self.__dict__
                else:
                    a[strings] = self.__dict__[strings]
            return a

            

                    
