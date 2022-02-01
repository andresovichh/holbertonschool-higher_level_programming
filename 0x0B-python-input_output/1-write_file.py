#!/usr/bin/python3

"""
Module that writes a string to a text file"""


def write_file(filename="", text=""):
    """ Writes to a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        length = f.write(text)
        return length
