#!/usr/bin/python3

""" Module that appends to a file"""


def append_write(filename="", text=""):
    """ appends a string to the end of a file"""
    with open(filename, 'a', encoding='UTF-8') as f:
        chars = f.write(text)
        return chars
