#!/usr/bin/python3
for first in range(0, 10):
    for last in range(first + 1, 10):
        if first == 8 and last == 9:
            print("{0:d}{1:d}".format(first, last))
        else:
            print("{0:d}{1:d}".format(first, last), end=", ")
