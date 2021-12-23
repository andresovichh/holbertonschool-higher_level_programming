#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    it = 0
    for argst in range(1, len(sys.argv)):
        it += int(sys.argv[argst])
        print("{}".format(it))
