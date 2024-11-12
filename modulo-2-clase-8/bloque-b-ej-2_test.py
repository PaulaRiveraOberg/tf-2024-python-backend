import unittest
from geopy.distance import geodesic

# Implementación de las clases Position y Distance para pruebas
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
        return geodesic(
            (self.source.latitud, self.source.longitud),
            (self.destination.latitud, self.destination.longitud)
        ).km

# Implementación de los casos de prueba
class TestPositionAndDistance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Crear posiciones para pruebas
        cls.pos1 = Position(0, 0, 0)
        cls.pos2 = Position(10, 10, 0)
        cls.pos_limit = Position(90, 180, 0)

    @classmethod
    def tearDownClass(cls):
        # Limpiar las posiciones creadas
        del cls.pos1
        del cls.pos2
        del cls.pos_limit

    # Pruebas para la clase Position
    def test_position_creation_validas(self):
        # Valores válidos
        pos = Position(45, 45, 100)
        self.assertEqual(pos.latitud, 45)
        self.assertEqual(pos.longitud, 45)
        self.assertEqual(pos.altitud, 100)

    def test_position_latitud_invalid_type(self):
        # Excepción esperada por tipo incorrecto en latitud
        with self.assertRaises(TypeError):
            Position("45", 45, 100)

    def test_position_longitud_invalid_type(self):
        # Excepción esperada por tipo incorrecto en longitud
        with self.assertRaises(TypeError):
            Position(45, "45", 100)

    def test_position_latitud_out_of_bounds(self):
        # Excepción esperada por latitud fuera de límites
        with self.assertRaises(ValueError):
            Position(-91, 45, 100)

    def test_position_longitud_out_of_bounds(self):
        # Excepción esperada por longitud fuera de límites
        with self.assertRaises(ValueError):
            Position(45, 181, 100)

    def test_position_edge_values(self):
        # Valores límite
        pos = Position(90, 180, 1000)
        self.assertEqual(pos.latitud, 90)
        self.assertEqual(pos.longitud, 180)
        self.assertEqual(pos.altitud, 1000)

    # Pruebas para la clase Distance
    def test_distance_km(self):
        # Comprobación de distancia en km entre dos posiciones
        dist = Distance(self.pos1, self.pos2)
        calculated_distance = geodesic((self.pos1.latitud, self.pos1.longitud), 
                                       (self.pos2.latitud, self.pos2.longitud)).km
        self.assertAlmostEqual(dist.km(), calculated_distance, places=5)

    def test_distance_same_position(self):
        # Distancia entre una posición y ella misma debe ser 0
        dist = Distance(self.pos1, self.pos1)
        self.assertEqual(dist.km(), 0)

# Ejecución de las pruebas
if __name__ == '__main__':
    unittest.main()