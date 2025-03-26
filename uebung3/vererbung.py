import math


class Punkt:

    def __init__(self, x=0.0, y=0.0):
        self.x = self._check_nummmer(x)
        self.y = self._check_nummmer(y)

    def _check_nummmer(self, wert):
        if not type(wert) == int and not type(wert) == float:
            raise TypeError(f"Wert muss eine Zahl sein, ist aber {type(wert)}.")
        return wert

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distanz(self, punkt):
        if not type(punkt) == Punkt:
            raise TypeError(f"Muss vom Typ Punkt sein, ist aber {type(punkt)}")
        return math.sqrt((punkt.x - self.x) ** 2 + (punkt.y - self.y) ** 2)


class Figur:

    def __init__(self, name, punkte):
        self.name = name
        self.punkte = punkte
        self._check_punkte()

    def _check_punkte(self):
        if not type(self.punkte) == list:
            raise TypeError(f"Muss eine Liste sein, ist aber {type(self.punkte)}")
        for punkt in self.punkte:
            if not type(punkt) == Punkt:
                raise TypeError(f"Muss vom Typ Punkt sein, ist aber {type(punkt)}.")

    def __str__(self):
        punkte_str = ', '.join([str(punkt) for punkt in self.punkte])
        return f"{self.name}: {punkte_str}"

    def umfang(self):
        summe = 0
        laenge = len(self.punkte)
        for i in range(laenge):
            punkt1 = self.punkte[i]
            punkt2 = self.punkte[(i + 1) % laenge]
            summe += punkt1.distanz(punkt2)
        return summe


class Dreieck(Figur):

    def __init__(self, punkt1, punkt2, punkt3):
        punkte = [punkt1, punkt2, punkt3]
        super().__init__('Dreieck', punkte)


class Rechteck(Figur):

    def __init__(self, obenlinks, untenrechts):
        punkte = [
            obenlinks,
            Punkt(untenrechts.x, obenlinks.y),
            untenrechts,
            Punkt(obenlinks.x, untenrechts.y),
        ]
        super().__init__('Rechteck', punkte)

    def __str__(self):
        return f"{self.name}: {self.punkte[0]} - {self.punkte[2]}"


class Kreis(Figur):

    def __init__(self, mitte, radius):
        punkte = [mitte]
        super().__init__('Kreis', punkte)
        self.radius = self._check_radius(radius)

    def _check_radius(self, radius):
        if not type(radius) == int and not type(radius) == float:
            raise TypeError(f"Radius muss eine Zahl sein.")
        if radius < 0:
            raise ValueError(f"Radius muss positiv sein.")
        return radius

    def umfang(self):
        return 2 * self.radius * math.pi

    def __str__(self):
        return f"{self.name}: M={self.punkte[0]}, r={self.radius}"


class Polygon(Figur):

    def __init__(self, *punkte):
        super().__init__('Polygon', list(punkte))


p02 = Punkt(0, 2)
p04 = Punkt(0, 4)
p40 = Punkt(4, 0)
p42 = Punkt(4, 2)
p44 = Punkt(4, 4)
p60 = Punkt(6, 0)
p64 = Punkt(6, 4)

dreieck = Dreieck(p04, p40, p64)
print(dreieck, f"-> Umfang={dreieck.umfang():.1f}")

rechteck = Rechteck(p02, p44)
print(rechteck, f"-> Umfang={rechteck.umfang():.1f}")

kreis = Kreis(p42, 3)
print(kreis, f"-> Umfang={kreis.umfang():.1f}")

polygon = Polygon(p02, p42, p40, p60, p64, p04)
print(polygon, f"-> Umfang={polygon.umfang():.1f}")
