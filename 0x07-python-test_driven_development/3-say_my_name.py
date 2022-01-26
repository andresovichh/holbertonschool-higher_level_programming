#!/usr/bin/python3
"""
A foo that takes two args and prints
My name is <first name> <last name> to stdout
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: print name to stdout
    Args
    first_name (str): str to prt name
    last_name (str): str to prt last name
    Error:
    if either last_name or first name not str: TypeError
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
