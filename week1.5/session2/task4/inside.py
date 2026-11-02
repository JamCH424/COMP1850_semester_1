# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class

import geometry

P1 = geometry.Point(1,1)
C = geometry.Circle(5, P1)
P2 = geometry.Point(1,1)

if P2 in C == True:
    print("The point is in C")
else:
    print("The point is not in C")
