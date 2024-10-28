import geopy.distance


class Position:
    def __init__(self, latitud, longitud, altitud):
        if not isinstance(latitud, int):
            raise TypeError("Latitud debe ser un numero")
        if not isinstance(longitud, int):
            raise TypeError("Longitud debe ser un numero")
        if latitud < -90 or latitud > 90:
            raise ValueError(f"Latitud inválida: {latitud}. Debe estar en el rango [-90, 90].")
        if longitud < -180 or longitud > 180:
            raise ValueError(f"Longitud inválida: {longitud}. Debe estar en el rango [-180, 180].")
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

    def __str__(self):
        return f"latitud: {self.latitud}, longitud: {self.longitud}, altitud: {self.altitud}"


class Distance:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def km(self):
        return geopy.distance.geodesic(
            (self.source.latitud, self.source.longitud),
            (self.destination.latitud, self.destination.longitud)
        ).km


# Intenta crear posición inválida
try:
    wrong = Position(100, 0, 0)
except ValueError as e:
    print(f"Excepción: {type(e).__name__} - {e}")


# Intenta crear posición no numerica
try:
    wrong = Position('100','0', 0)
except TypeError as e:
    print(f"Excepción: {type(e).__name__} - {e}")
