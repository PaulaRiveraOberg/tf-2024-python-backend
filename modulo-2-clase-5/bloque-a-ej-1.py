lista = [1, 2, 3, 4, 5, "a"]

# https://docs.python.org/3/library/exceptions.html#concrete-exceptions
print("Excepciones con Listas")
# Algunos ejemplos
# IndexError: Acceder a un índice que no existe
try:
    lista[10]
except IndexError as e:
    print(f"Excepción: {type(e).__name__} - {e}")

# ValueError: Elemento no existente
try:
    lista.remove(22)
except ValueError as e:
    print(f"Excepción: {type(e).__name__} - {e}")

# TypeError: Elementos no comparables str and int
try:
    lista.sort()
except TypeError as e:
    print(f"Excepción: {type(e).__name__} - {e}")

print("Excepciones con Diccionarios")
# Ejemplos
diccionario = {"nombre": "Roberto", "edad": 40}

# KeyError: clave no existente
try:
    diccionario["direccion"]
except KeyError as e:
    print(f"Excepción: {type(e).__name__} - {e}")

# TypeError: tipo de dato no permitido como clave
try:
    diccionario[['direccion']] = 'error'
except TypeError as e:
    print(f"Excepción: {type(e).__name__} - {e}")

# AttributeError: objeto no tiene el atributo
try:
    diccionario.mykeys()
except AttributeError as e:
    print(f"Excepción: {type(e).__name__} - {e}")