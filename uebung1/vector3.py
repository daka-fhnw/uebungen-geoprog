import math


class Vector3:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def len(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)


def test(x, y, z):
    v = Vector3(x, y, z)
    print(f'Vektor ({x}, {y}, {z}) hat Länge {v.len():.2f}')


test(0, 0, 0)
test(1, 2, 3)
test(3, 7, 6)
