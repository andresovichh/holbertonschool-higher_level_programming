#!/usr/bin/python3

array = []
i = 0
while i < 1000000:
    array.append(1)
    i += 1
i = 0
for i in range(len(array)):
    array[i] = array[i] * len(array)
print(array)