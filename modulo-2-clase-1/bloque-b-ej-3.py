# grupal bloque B - 3
def enRango(min, max, valor):
    if valor >= min and valor <= max:
        return True
    else:
        return False

print(enRango(5, 10, 7)) #true
print(enRango(5, 10, 11)) #false