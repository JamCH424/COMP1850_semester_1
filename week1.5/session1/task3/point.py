# Week 1.5, Session 1: Task 3

import math

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

# Finally, add code here to demonstrate use of Point

p = Point(4,3)
print(p.distance())

q = Point(0,1)
print(p.distance_to(q))
