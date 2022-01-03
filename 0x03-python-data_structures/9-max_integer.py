#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        my_list.sort()
        a = len(my_list)
        return my_list[a -1]
