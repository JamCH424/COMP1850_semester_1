# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

import shapes

p = shapes.Point(1,2)
C = shapes.Circle(5,p)

C.set_radius(4)
print(C)
print(C.area())
print(C.perimeter())