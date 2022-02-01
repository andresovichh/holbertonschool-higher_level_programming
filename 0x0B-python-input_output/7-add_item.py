#!/usr/bin/python3
"""
returns the JSON representation of an object (string):"""

from sys import argv
""" import argv module"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    f = load_from_json_file("add_item_json" + argv[1:])
    save_to_json_file(f, "add_item_json")
except:
    something