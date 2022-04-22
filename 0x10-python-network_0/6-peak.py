#!/usr/bin/python3


"""
this is a function to find the peaks"""


def find_peak(list_of_integers):
    """ this is a foo that finds a peak"""

    sorted_list = []
    if len(list_of_integers) == 0:
        return None
    else:
        sorted_list = sorted(list_of_integers)

        return (sorted_list[len(sorted_list) - 1])
