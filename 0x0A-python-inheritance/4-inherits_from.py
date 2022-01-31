#!/usr/bin/python3
"""
Module that checks if the obj is an instance of a class that inherited
(directly or indirectly) from the specified class """


def inherits_from(obj, a_class):
    """
    Method that returns true or false
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        print(type(obj))
        print(type(a_class))
        return True
    else:
        print(type(obj))
        print(type(a_class))
        return False
