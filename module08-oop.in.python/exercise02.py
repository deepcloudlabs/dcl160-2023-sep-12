import math
from random import randint


class square:
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        print(f"square::area()")
        return self.edge * self.edge


class cube(square):
    def __init__(self, edge):
        super().__init__(edge)

    def area(self):
        print(f"cube::area()")
        return 6 * self.edge * self.edge


class circle(square):
    def __init__(self, edge):
        super().__init__(edge)

    def area(self):
        print(f"circle::area()")
        return math.pi * self.edge / 4.


coin = randint(0, 2)
if coin == 0:
    shape = cube(2)
elif coin == 1:
    shape = square(2)
else:
    shape = circle(2)

print(f"shape's ({type(shape)}) area is {shape.area()}")
