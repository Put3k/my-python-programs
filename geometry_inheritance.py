import math


class Polygon:
    def __init__(self):
        pass
    def get_area():
        raise NotImplementedError()
    def get_sides():
        raise NotImplementedError()
    def get_perimeter():
        raise NotImplementedError()   #do poprawy później
    


class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        A = math.sqrt(s*(s - a) * (s - b) * (s - c))
        return A

    def get_sides(self):
        return [self.a, self.b, self.c]

    def get_perimeter(self):
        P = self.a + self.b + self.c
        return P


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        self.A = self.width * self.height
        return self.A

    def get_sides(self):
        self.sides = 2*[self.width, self.height]
        return self.sides

    def get_perimeter(self):
        self.P = (self.width) * 2 + (self.height) * 2
        return self.P 


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

square = Square(3)
print(square.get_sides())
