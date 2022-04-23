#!/usr/bin/python3


"""
this is a function to find the peaks"""


def find_peak(list_of_integers):
    """ this is a foo that finds a peak"""

    peak = 0
    for i in list_of_integers:
        if (i + 1) > i and (i + 1) < (i+ 2):
            peak = i
    return peak