class Position:
    def __init__(self, latitud, longitud, altitud):
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

    def __str__(self):
        return f"latitud: {self.latitud}, longitud: {self.longitud}, altitud: {self.altitud}"

class Waypoint(Position):
    def __init__(self, latitud, longitud, altitud, nombre):
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud
        self.nombre = nombre

    def __str__(self):
        return f"Waypoint(nombre: {self.nombre}, {super().__str__()})"

class Trackpoint(Position):
    def __init__(self, latitud, longitud, altitud, fecha):
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud
        self.fecha = fecha

    def __str__(self):
        return f"Trackpoint(Fecha: {self.fecha}, {super().__str__()})"

waypoint = Waypoint(-33.047237, -71.612686, 10, "Valparaiso")
print(waypoint)

trackpoint = Trackpoint(-33.047237, -71.612686, 10, "2024-10-22 10:30:00")
print(trackpoint)