class Vector3:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if type(other) == Vector3:
            return self._comp_mul(other)
        elif type(other) == int or type(other) == float:
            return self._scalar_mul(other)
        else:
            raise TypeError(f"Parameter muss Vector3 oder scalar sein, ist aber {type(other)}.")

    def __rmul__(self, other):
        return self._scalar_mul(other)

    def _comp_mul(self, other):
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def _scalar_mul(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def len(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def cross(self, other):
        if not type(other) == Vector3:
            raise TypeError(f"Parameter muss Vector3 sein, ist aber {type(other)}.")
        x = (self.y * other.z) - (self.z * other.y)
        y = (self.z * other.x) - (self.x * other.z)
        z = (self.x * other.y) - (self.y * other.x)
        return Vector3(x, y, z)

    def dot(self, other):
        if not type(other) == Vector3:
            raise TypeError(f"Parameter muss Vector3 sein, ist aber {type(other)}.")
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return x + y + z

    def normalize(self):
        length = self.len()
        if length > 0:
            return self._scalar_mul(1 / length)
        else:
            return self
