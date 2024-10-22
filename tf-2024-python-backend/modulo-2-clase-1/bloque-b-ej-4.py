# grupal bloque B - 4
FIN = False
mayor = float("-inf")
while not FIN:
    valor = input()
    if valor == "FIN":
        FIN = True
    else:
        if float(valor) > mayor:
            mayor = float(valor)

    print("mayor hasta ahora es", mayor)