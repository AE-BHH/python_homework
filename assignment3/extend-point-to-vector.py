import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    

    def __str__(self):
        return f"Parent({self.x}, {self.y})"
    
    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Vector(Point):
    
    def __str__(self):
        return f"child class {self.x}, {self.y}"
        
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
p1 = Point(2, 3)
p2 = Point(2, 3)

print("P1", p1)
print("P2", p2)
print("Are P1 and P2 equal?", p1 == p2)
print("Distance from P1 to P2", p1.distance_to(p2))

print()

v1 = Vector(1, 3)
v2 = Vector(2, 4)

print("v1", v1)
print("v2", v2)
v3 = v1 + v2
print("v1 + v2", v3)
print("Are v1 and v2 equal?", v1 == v2)
print("Distance from v1 to v2", v1.distance_to(v2))

