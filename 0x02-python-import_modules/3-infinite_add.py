#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    for args in range(len(sys.argv) -1):
        i += int(sys.argv[args +1])
        print("{}".format(i)))
