#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary[key]:
        a_dictionary[key] = None
    return a_dictionary
