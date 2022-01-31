#!/usr/bin/python3

"""
Module that checks if type is exactly an instance
of the specified class"""

def is_same_class(obj, a_class):
    """
    Returns true if obj is exactly na instance
    of the specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
