# All cunfions/variable of formalt __name__ are magic or dunder functions and has a special place in python.

import math

class Circle:
    # Constructor/init.
    def __init__(self, radius):
        self.r = radius
        self.r > radius
        
    # Method get_Area
    def get_area(self):
        return self.r**2*math.pi
    
    # Methrod set_radios
    def set_radius(self, r):
        self.r = r
    
    # magic function __lt__ is used to define the behaviour of operator less than < on the class Circle.
    def __lt__(self, other):
        return self.r < other.r
    
    # magic function __lt__ is used to define the behaviour of operator greater than > on the class Circle.
    def __gt__(self, other):
        return self.r > other.r
    
    # magic function __lt__ is used to define the behaviour of operator equals == on the class Circle.
    def __eq__(self, other):
        return self.r == other.r

circle = Circle(1)
print("Set radius to 5")
circle.set_radius(5)
print(circle.r)
circle.set_radius(5,6)
print(circle.r)


print("this is a file with a class")
print(circle.get_area())

c1 = Circle(5)
c2 = Circle(20)
print(c1<c2)

# we can do this because we defined __lt__ in Circle.
if c1 < c2:
    print("c1 is smaller")

list_of_circles = [c1, c2, circle]
list_of_circles.sort()	# Sort can be used because we defined __lt__ (also __gt__, __eq__) is good to define for default functions.