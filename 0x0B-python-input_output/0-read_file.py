#!/usr/bin/python3

"""
Module that reads a text file UTF8"""


def read_file(filename=""):
    """ Reads a file with 'with'
    Args:
        filename (str): filename to open
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read())
