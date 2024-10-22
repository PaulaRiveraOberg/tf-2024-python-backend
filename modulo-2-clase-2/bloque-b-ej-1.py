personas = []

while True:
    nombre = input("Ingresa el nombre (o escribe 'FIN' para terminar): ")
    if nombre.upper() == "FIN":
        break
    apellido = input("Ingresa el apellido: ")
    persona = {"nombre": nombre, "apellido": apellido}
    personas.append(persona)

# Mostramos la lista completa de personas registradas
print("\nLista de personas registradas:")
for persona in personas:
    print(f"Nombre: {persona['nombre']}, Apellido: {persona['apellido']}")
