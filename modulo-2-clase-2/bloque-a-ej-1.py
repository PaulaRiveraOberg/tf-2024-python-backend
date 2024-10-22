mi_lista = [10, 20, 5, 60, 20, 10]


def stats(lista):
    print("El rango es min:", min(lista), " max:", max(lista))
    suma = 0
    n = 0
    for numero in lista:
        suma += numero
        n += 1
    promedio = suma / n
    print("El promedio es:", promedio)
    print(
        "El promedio mediante funciones genéricas es:",
        (float(sum(lista)) / len(lista)),
    )


stats(mi_lista)
