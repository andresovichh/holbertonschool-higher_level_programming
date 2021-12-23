#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0")
    elif len(sys.argv) == 2:
        print("1")
    else:
        print("{:d}".format(int(len(sys.argv) - 1)))
        if len(sys.argv) > 1:
            for i in range(1, len(sys.argv)):
                print("{:d}".format(int(sys.argv[i])))
