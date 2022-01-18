#!/usr/bin/python3
class Robot(object):
    pass
x = Robot()
Robot.brand = "Kuka"
x.brand = "Thales"
print(Robot.brand)
y = Robot()
print(y.brand)
Robot.brand = "Thales"
print(y.brand)
print(x.__dict__)
print(y.__dict__)
print(Robot.__dict__)
print(x.energy)