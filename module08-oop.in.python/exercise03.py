import math


class shape:  # interface
    def draw(self):
        pass

    def area(self):
        pass

    def circumference(self):
        pass


class square(shape):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        print(f"square::area()")
        return self.edge * self.edge

    def draw(self):
        print("Drawing a square...")

    def circumference(self):
        return 4. * self.edge


class cube(shape):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        print(f"cube::area()")
        return 6 * self.edge * self.edge

    def draw(self):
        print("Drawing a cube...")

    def circumference(self):
        return 12. * self.edge


class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"circle::area()")
        return math.pi * self.radius * self.radius

    def draw(self):
        print("Drawing a circle...")

    def circumference(self):
        return 2. * math.pi * self.radius
