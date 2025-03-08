import unittest

from vector3 import Vector3


class TestVector3(unittest.TestCase):

    def test_empty(self):
        vector = Vector3()
        self._verify(vector, 0, 0, 0, 0)

    def test_zeros(self):
        self._create_and_verify(0, 0, 0, 0)

    def test_len_1(self):
        self._create_and_verify(2, 1, 2, 3)

    def test_len_2(self):
        self._create_and_verify(3, 4, 12, 13)

    def _verify(self, vector, x, y, z, v_len):
        self.assertEqual(vector.x, x)
        self.assertEqual(vector.y, y)
        self.assertEqual(vector.z, z)
        self.assertEqual(vector.len(), v_len)

    def _create_and_verify(self, x, y, z, v_len):
        vector = Vector3(x, y, z)
        self._verify(vector, x, y, z, v_len)


if __name__ == '__main__':
    unittest.main()
