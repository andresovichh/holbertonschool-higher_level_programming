#!/usr/bin/python3
def fizzbuzz():
    i = 0
    for i in range(0, 101):
        if (i % 3 == 0):
            print("{}".format("Fizz"))
        elif (i % 5 == 0):
            print("{}".format("Buzz"))
        elif((i % 3 == 0) and (i % 5 == 0)):
            print("{}".format("FizzBuzz"))
        else:
            print("{}".format(i))

