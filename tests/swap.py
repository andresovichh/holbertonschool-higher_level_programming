#!/usr/bin/python3

from tempfile import tempdir


def swap(a, b):
    # temporary swap
    print("a = {} b = {}". format(a, b))
    tmp = a
    a = b
    b = tmp
    del tmp
    print("a = {} b = {}". format(a, b))

def tuple_swap(a, b):
    a, b = b, a
    print("a = {} b = {}". format(a, b))
swap(6, 7)
tuple_swap(6, 7)