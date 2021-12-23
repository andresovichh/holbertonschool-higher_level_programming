#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    for argst in range(len(sys.argv) - 1):
        i += int(sys.argv[argst + 1])
        print("{}".format(i))
