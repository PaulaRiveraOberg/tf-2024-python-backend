distancia_euclidiana = lambda x1, y1, x2, y2: ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Ingresar las coordenadas por la entrada estándar
x1 = float(input("Ingrese la coordenada x1: "))
y1 = float(input("Ingrese la coordenada y1: "))
x2 = float(input("Ingrese la coordenada x2: "))
y2 = float(input("Ingrese la coordenada y2: "))

resultado = distancia_euclidiana(x1, y1, x2, y2)
print(
    f"La distancia euclidiana entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {resultado}"
)

#  EJEMPLO
# P1 = (0,0)
# P2 = (3,4)
# => D = 5
