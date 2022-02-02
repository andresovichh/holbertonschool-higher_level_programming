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

    def to_json(self):
        """
        retrieves a dictionary """
        return self.__dict__
