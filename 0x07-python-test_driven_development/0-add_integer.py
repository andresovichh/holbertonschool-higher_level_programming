#!usr/bin/python3

"""
This module adds integers, with one foo, add_integer()
For example,
>>> add_integer(30, 5)
35
"""

def add_integer(a, b=98):
    """ Return the addition of two integers

    Args:
        a (int): an int
        b (int): another int

    Returns:
        An int with the addition

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)