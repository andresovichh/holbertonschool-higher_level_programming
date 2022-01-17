#!/usr/bin/python3
def safe_function(fct, *args):
    import sys


    try:
        return fct(*args)
        