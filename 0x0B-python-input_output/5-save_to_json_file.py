#!/usr/bin/python3
"""
returns the JSON representation of an object (string):"""
import json


def save_to_json_file(my_obj, filename):
    """ Returns the def to_json_string(my_obj):"""
    with open(filename, 'w', encoding='UTF-8') as f:
       json.dump(my_obj, f)
