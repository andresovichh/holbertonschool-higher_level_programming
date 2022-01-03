#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = (len(my_list))
    if my_list:
        while i:
            print("{:d}".format(i))
            i -= 1

