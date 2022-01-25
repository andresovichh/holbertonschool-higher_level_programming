#!/usr/bin/python3

def prt_horseman(horsemen):
     for horseman in horsemen:
        print(horsemen[1])
     for fruit in ["banana", "apple", "quince"]:
        print("I like to eat " + fruit + "s!")
     numbers = [1, 2, 3, 4, 5, 6]
     for index, value in enumerate(numbers):
         numbers[index] = value ** 2
     print(numbers)
     horsemens = ["andres", ["patricio", "juan maria"], {("ok", 1), "no"}]
     for index, value in enumerate(horsemens):
         print(index, value)
     print(horsemen[1][1])
horsemen = ["andres", ["patricio", "juan maria"], {("ok", 1), "no"}]


prt_horseman(horsemen)