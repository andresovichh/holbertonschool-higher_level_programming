#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a_list = my_list[:]
    if idx < 0 or idx > len(a_list):
        return my_list
    elif my_list and a_list:
        a_list[idx] = element
        return a_list
