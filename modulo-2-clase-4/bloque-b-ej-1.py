from functools import reduce

# split permite dividir una cadena en una lista, luego con map obtenemos una lista de enteros
numeros = list(
    map(int, input("Ingrese una lista de números separados por espacios: ").split())
)

resultado = reduce(lambda x, y: x if x > y else y, numeros)

print(f"El valor mayor en la lista es: {resultado}")
