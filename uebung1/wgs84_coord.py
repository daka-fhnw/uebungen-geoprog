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
