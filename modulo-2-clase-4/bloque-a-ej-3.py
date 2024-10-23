import geopy.distance

class Position:
    def __init__(self, latitud, longitud, altitud):
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

# Valparaiso
pos1 = Position(-33.047237, -71.612686, 10)
# Santiago
pos2 = Position(-33.447487, -70.673676, 520)

distance = Distance(pos1, pos2)
print(f"La distancia geodésica es de {distance.km():.2f} km.")
