import unittest

from vector3 import Vector3


class TestVector3(unittest.TestCase):

    def _verify_vector(self, vector, x, y, z):
        self.assertEqual(x, vector.x)
        self.assertEqual(y, vector.y)
        self.assertEqual(z, vector.z)

    def test_empty(self):
        vector = Vector3()
        self._verify_vector(vector, 0, 0, 0)

    def test_zeros(self):
        vector = Vector3(0, 0, 0)
        self._verify_vector(vector, 0, 0, 0)

    def test_values(self):
        vector = Vector3(1, 2, 3)
        self._verify_vector(vector, 1, 2, 3)

    def test_len_0(self):
        vector = Vector3(0, 0, 0)
        self.assertEqual(0, vector.len())

    def test_len_1(self):
        vector = Vector3(2, 1, 2)
        self.assertEqual(3, vector.len())

    def test_len_2(self):
        vector = Vector3(3, 4, 12)
        self.assertEqual(13, vector.len())

    def test_str_1(self):
        vector = Vector3(1, 2, 3)
        self.assertEqual("(1, 2, 3)", str(vector))

    def test_str_2(self):
        vector = Vector3(-31.1, -22.2, -13.3)
        self.assertEqual("(-31.1, -22.2, -13.3)", str(vector))

    def test_add(self):
        vector1 = Vector3(1, 2, 3)
        vector2 = Vector3(3, 4, 5)
        result = vector1 + vector2
        self._verify_vector(result, 4, 6, 8)

    def test_sub(self):
        vector1 = Vector3(6, 5, 4)
        vector2 = Vector3(1, 2, 3)
        result = vector1 - vector2
        self._verify_vector(result, 5, 3, 1)

    def test_mul_comp(self):
        vector1 = Vector3(2, 3, 4)
        vector2 = Vector3(3, 4, 5)
        result = vector1 * vector2
        self._verify_vector(result, 6, 12, 20)

    def test_mul_scalar_1(self):
        scalar = 3
        vector = Vector3(1, 2, 3)
        result = vector * scalar
        self._verify_vector(result, 3, 6, 9)

    def test_mul_scalar_2(self):
        scalar = 3
        vector = Vector3(1, 2, 3)
        result = scalar * vector
        self._verify_vector(result, 3, 6, 9)

    def test_cross_1(self):
        vector1 = Vector3(3, 1, 0)
        vector2 = Vector3(-1, 1, 0)
        result = vector1.cross(vector2)
        self._verify_vector(result, 0, 0, 4)

    def test_cross_2(self):
        vector1 = Vector3(4, 2, -5)
        vector2 = Vector3(0, 4, 6)
        result = vector1.cross(vector2)
        self._verify_vector(result, 32, -24, 16)

    def test_cross_3(self):
        vector1 = Vector3(2, 1, 4)
        vector2 = Vector3(3, 2, 7)
        result = vector1.cross(vector2)
        self._verify_vector(result, -1, -2, 1)

    def test_dot_1(self):
        vector1 = Vector3(2, -6, 4)
        vector2 = Vector3(-1, 2, 3)
        result = vector1.dot(vector2)
        self.assertEqual(-2, result)

    def test_dot_2(self):
        vector1 = Vector3(-1, 3, 0.5)
        vector2 = Vector3(2, -1.5, -1)
        result = vector1.dot(vector2)
        self.assertEqual(-7.0, result)

    def test_normalize_1(self):
        vector = Vector3(6, 3, 6)
        result = vector.normalize()
        self.assertEqual(1, result.len())
        self._verify_vector(result, 2 / 3, 1 / 3, 2 / 3)

    def test_normalize_2(self):
        vector = Vector3(1, 0, 0)
        result = vector.normalize()
        self.assertEqual(1, result.len())
        self._verify_vector(result, 1, 0, 0)


if __name__ == '__main__':
    unittest.main()
