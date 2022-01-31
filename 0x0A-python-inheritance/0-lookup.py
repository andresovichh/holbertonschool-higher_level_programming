#!/usr/bin/python3
"""
Module to return the list of available attributes
and methods of an object """
def lookup(obj):
    """
    Returns the object's methods and attribtues"""
    return (list(dir(obj)))
