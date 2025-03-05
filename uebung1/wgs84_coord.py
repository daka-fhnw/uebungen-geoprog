class WGS84Coord:

    def __init__(self, longitude=0, latitude=0):
        self.longitude = longitude
        self.latitude = latitude

    def set_longitude(self, value):
        fixed = value
        if value < -180 or value > 180:
            fixed = ((value + 180) % 360) - 180
            print(f'Warnung: Länge wurde korrigiert von {value}° zu {fixed}°.')
        self._longitude = fixed

    def get_longitude(self):
        return self._longitude

    longitude = property(get_longitude, set_longitude)

    def set_latitude(self, value):
        fixed = value
        if value < -90 or value > 90:
            fixed = max(-90, min(90, value))
            print(f'Warnung: Breite wurde korrigiert von {value}° zu {fixed}°.')
        self._latitude = fixed

    def get_latitude(self):
        return self._latitude

    latitude = property(get_latitude, set_latitude)


def line():
    print(10 * '---')


def test(lon, lat):
    print(f'> Input: {lon}°, {lat}°')
    c1 = WGS84Coord()
    c1.longitude = lon
    c1.latitude = lat
    print(f'> Variante 1: {c1.longitude}°, {c1.latitude}°')
    c2 = WGS84Coord(lon, lat)
    print(f'> Variante 2: {c2.longitude}°, {c2.latitude}°')
    line()


line()
test(0, 0)
test(10, 30)
test(-180, 90)
test(180, -90)
test(-200, 100)
test(200, -100)
test(360, 0)
test(-360, 0)
test(1080, 0)
test(-1080, 0)
test(1125, 0)
test(-1125, 0)
