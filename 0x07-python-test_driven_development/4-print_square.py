#!/usr/bin/python3
"""
Module that prints a square pattern to stdout
"""


def print_square(size):
    """
    Module that prints square pattern to stdout.

    Args:
    size (int): side of square
    """
    if (isinstance(size, float)) and (size < 0):
        raise TypeError("size must be an integer")
    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for i in range(size):
            print('#', end="")
        print()
