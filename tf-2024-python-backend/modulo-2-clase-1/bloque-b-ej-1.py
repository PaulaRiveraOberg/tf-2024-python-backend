# grupal bloque B - 1
## caso A - 1
def raiz_cuadrada(valor):
    raiz_cuadrada = valor ** (1 / 2)
    return raiz_cuadrada


valor = int(input())
print(raiz_cuadrada(valor))


## caso A - 2
def distancia(x1, x2, y1, y2):
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    return distancia

x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

print(distancia(x1, x2, y1, y2))

## caso A - 3
def invertir(palabra):
    palabra_invertida = palabra[::-1]
    return palabra_invertida

palabra = input()
print(invertir(palabra))
