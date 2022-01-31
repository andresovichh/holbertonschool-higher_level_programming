#!/usr/bin/python3

"""
Module is_kind_of_class that checks if obj is an isntence of or obj
is an instance of a class that inherited from the specified
class"""


def is_kind_of_class(obj, a_class):
    """
    Returns true or false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
