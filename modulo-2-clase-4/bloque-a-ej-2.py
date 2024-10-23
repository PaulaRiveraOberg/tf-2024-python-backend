class Position:
    def __init__(self, latitud, longitud, altitud):
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

    def __str__(self):
        return f"{self.latitud}, {self.longitud}, {self.altitud}"

    def __dict__(self):
        return {
            "latitud": self.latitud,
            "longitud": self.longitud,
            "altitud": self.altitud
        }

    def __str__(self):
        return f"latitud: {self.latitud}, longitud: {self.longitud}, altitud: {self.altitud}"

position = Position(40.7128, -74.0060, 10)

# Representación como cadena separada por comas
print(position)

# Representación como diccionario
print(position.__dict__())