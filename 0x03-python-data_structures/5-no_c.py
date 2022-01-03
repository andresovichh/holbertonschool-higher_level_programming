#!/usr/bin/python3
def no_c(my_string):
    res = my_string.translate({ord("c" and "C"): None})
    return res