import geopy.distance


# Clase que representa una posición geográfica con latitud, longitud y altitud
class Position:
    def __init__(self, latitud, longitud, altitud):
        # Validación de tipos de datos
        if not isinstance(latitud, int):
            raise TypeError("Latitud debe ser un numero")
        if not isinstance(longitud, int):
            raise TypeError("Longitud debe ser un numero")
        
        # Validación de rangos válidos
        if latitud < -90 or latitud > 90:
            raise ValueError(f"Latitud inválida: {latitud}. Debe estar en el rango [-90, 90].")
        if longitud < -180 or longitud > 180:
            raise ValueError(f"Longitud inválida: {longitud}. Debe estar en el rango [-180, 180].")
            
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

    def __str__(self):
        return f"latitud: {self.latitud}, longitud: {self.longitud}, altitud: {self.altitud}"


# Clase que calcula la distancia geodésica entre dos posiciones
class Distance:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def km(self):
        # Calcula la distancia en kilómetros usando geopy
        return geopy.distance.geodesic(
            (self.source.latitud, self.source.longitud),
            (self.destination.latitud, self.destination.longitud)
        ).km

# Función auxiliar para verificar el string de representación de una posición
def verifica_string_posiciones(posicion, latitud, longitud, altitud):
    if str(posicion) == f"latitud: {latitud}, longitud: {longitud}, altitud: {altitud}":
        print('El string de posicion es correcto')
    else:
        print('El string de posición es incorrecto')

# Test 1: Verifica que el método __str__ de Position funciona correctamente
# Sigue el patrón de 4 fases: setup, ejecución, verificación y cleanup
def test_str_posicion_valida():
    # setupUp - Preparación de datos de prueba
    latitud, longitud, altitud = 60, 0, 0
    
    # ejecucion - Creación del objeto a probar
    posicion = Position(latitud, longitud, altitud)
    
    # verificacion - Comprobación del resultado esperado
    verifica_string_posiciones(posicion, latitud, longitud, altitud)
    
    # cleanup - Limpieza de variables
    del latitud, longitud, altitud

# Función auxiliar para verificar si una distancia es cero
def verifica_es_distancia_cero(distancia):
    if distancia==0:
        print('La distancia es la esperada, 0')
    else:
        print('La distancia no es 0')

# Test 2: Verifica que la distancia entre un punto y sí mismo es cero
# También sigue el patrón de 4 fases
def test_distancia_mismo_punto_es_cero():
    # setupUp - Preparación de datos de prueba
    latitud, longitud, altitud = 60, 0, 0
    
    # ejecucion - Creación de objetos y cálculo de distancia
    position_1 = Position(latitud, longitud, altitud)
    position_2 = Position(latitud, longitud, altitud)
    distancia = Distance(position_1, position_2)
    
    # verificacion - Comprobación del resultado esperado
    res = distancia.km()
    verifica_es_distancia_cero(res)
    
    # cleanup - Limpieza de variables
    del latitud, longitud, altitud

# Ejecución de las pruebas
test_str_posicion_valida()
test_distancia_mismo_punto_es_cero()
