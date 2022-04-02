from math import sqrt
class Punto:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_string(self):
        return f"{self.x}, {self.y}, {self.z}"

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z

    def distance(self, p):
        d = (self.x - p.x)**2 + (self.y - p.y)**2 + (self.z - p.z)**2
        return sqrt(d)
        



punto = Punto(1,1,3)
print(punto.to_string())

punto.set_x(4)
punto.set_z(1)
print(punto.to_string())

punto1 = Punto(7,3,2)
print(punto1.to_string())
print(punto.distance(punto1))
