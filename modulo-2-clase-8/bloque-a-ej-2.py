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


# Clases de equivalencia para Position:
# 1. Latitud:
#   - CE1: Valores válidos (-90 <= latitud <= 90)
#   - CE2: Valores inválidos (latitud < -90 o latitud > 90) 
#   - CE3: Tipo de dato inválido (no entero)

# 2. Longitud:
#   - CE4: Valores válidos (-180 <= longitud <= 180)
#   - CE5: Valores inválidos (longitud < -180 o longitud > 180)
#   - CE6: Tipo de dato inválido (no entero)

# 3. Altitud:
#   - CE7: Cualquier valor numérico es válido

# Valores frontera para Position:
# - Latitud: -90, -89, 0, 89, 90
# - Longitud: -180, -179, 0, 179, 180

# Casos de prueba para Distance:
# 1. Distancia entre puntos en el mismo lugar (0 km)
# 2. Distancia entre puntos en hemisferios opuestos (máxima distancia)
# 3. Distancia entre puntos en el ecuador
# 4. Distancia entre puntos en el mismo meridiano
# 5. Distancia entre puntos en diferentes cuadrantes

def test_casos():
    # Casos de prueba para Position
    try:
        # Caso válido
        p1 = Position(0, 0, 0)
        print("Caso válido creado correctamente")
        
        # Casos frontera
        p2 = Position(-90, -180, 0)
        p3 = Position(90, 180, 0)
        print("Casos frontera creados correctamente")
        
        # Pruebas de distancia
        d1 = Distance(p1, p1)
        assert d1.km() == 0, "La distancia al mismo punto debe ser 0"
        
        d2 = Distance(p2, p3)
        print(f"Distancia máxima: {d2.km()} km")
        
    except (ValueError, TypeError) as e:
        print(f"Error en prueba: {str(e)}")

if __name__ == "__main__":
    test_casos()
