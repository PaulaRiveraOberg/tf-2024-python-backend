lista = [1,2,3,4,5,6,7,8,9,10]

def suma_cuadrado(lista_original):
    lista = lista_original.copy()
    for i in range(len(lista)):
        lista[i] = lista[i]*lista[i]
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

print(lista)
resultado = suma_cuadrado(lista)
print(resultado)
print(lista)
