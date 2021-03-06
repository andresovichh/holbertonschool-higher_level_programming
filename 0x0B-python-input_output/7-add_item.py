#!/usr/bin/python3
"""
returns the JSON representation of an object (string):"""

import json
from sys import argv
""" import argv module"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    f = load_from_json_file("add_item.json") + argv[1:]
    save_to_json_file(f, "add_item.json")
except:
    save_to_json_file(argv[1:], "add_item.json")
