#!/usr/bin/python3
def uppercase(str):
    i = 0;
    while(str[i] != 0):
        if(96 < ord(str[i]) < 123):
            print(ord(str[i])-32)
        elif(64 < ord(str[i]) < 91):
            print("{}".format(str))
