#!/usr/bin/python3
def no_c(my_string):
    res = my_string.translate({ord(c): None for c in "cC"})
    return res
