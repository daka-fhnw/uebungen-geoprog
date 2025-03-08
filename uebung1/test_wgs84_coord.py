import unittest

from wgs84_coord import WGS84Coord


class TestWGS84Coord(unittest.TestCase):

    def test_empty(self):
        coord = WGS84Coord()
        self._verify(coord, 0, 0)

    def test_constructor(self):
        self._create_and_verify(10, 30)

    def test_lon_valid(self):
        self._create_and_verify(180, 0)

    def test_lon_valid_2(self):
        self._create_and_verify(-180, 0)

    def test_lon_wrap_1(self):
        self._create_and_verify(200, 0, -160, 0)

    def test_lon_wrap_2(self):
        self._create_and_verify(-200, 0, 160, 0)

    def test_lon_wrap_3(self):
        self._create_and_verify(360, 0, 0, 0)

    def test_lon_wrap_4(self):
        self._create_and_verify(-360, 0, 0, 0)

    def test_lon_wrap_5(self):
        self._create_and_verify(1080, 0, 0, 0)

    def test_lon_wrap_6(self):
        self._create_and_verify(-1080, 0, 0, 0)

    def test_lon_wrap_7(self):
        self._create_and_verify(1125, 0, 45, 0)

    def test_lon_wrap_8(self):
        self._create_and_verify(-1125, 0, -45, 0)

    def test_lat_valid_1(self):
        self._create_and_verify(0, 90)

    def test_lat_valid_2(self):
        self._create_and_verify(0, -90)

    def test_lat_limit_1(self):
        self._create_and_verify(0, 100, 0, 90)

    def test_lat_limit_2(self):
        self._create_and_verify(0, -100, 0, -90)

    def _verify(self, coord, lon, lat):
        self.assertEqual(coord.longitude, lon)
        self.assertEqual(coord.latitude, lat)

    def _create_and_verify(self, lon, lat, exp_lon=None, exp_lat=None):
        v_lon = exp_lon if exp_lon is not None else lon
        v_lat = exp_lat if exp_lat is not None else lat
        # variant 1
        coord1 = WGS84Coord(lon, lat)
        self._verify(coord1, v_lon, v_lat)
        # variant 2
        coord2 = WGS84Coord(lon, lat)
        coord2.longitude = lon
        coord2.latitude = lat
        self._verify(coord2, v_lon, v_lat)


if __name__ == '__main__':
    unittest.main()
