#!/usr/bin/python3
"""
returns the JSON representation of an object (string):"""
import json


def load_from_json_file(filename):
    """ Returns the def to_json_string(my_obj):"""
    with open(filename, encoding='UTF-8') as f:
        i = json.load(f)
    return (i)
