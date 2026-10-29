# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    # Add distance() method here
    def distance(self):
        distance = math.sqrt(self.x**2 + self.y**2)

        return distance
        
    # Add distance_to() method here

    def distance_to(self, other_point):
        # Distance between two points
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance
    
    # (This will need a parameter representing another point)
# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

class Circle:

    def __init__(self, centre, radius):
        self.radius = radius
        self.centre = centre

    def area(self):
        area = math.pi * (self.radius **2)

        return area

    def perimeter(self):
        perimeter = math.pi * self.radius * 2

        return perimeter

# Don't add any testing code to this file!
