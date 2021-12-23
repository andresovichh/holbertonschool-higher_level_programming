#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = 0
    for argst in range(1, len(sys.argv)):
        i += int(sys.argv[argst])
        print("{}".format(i))
