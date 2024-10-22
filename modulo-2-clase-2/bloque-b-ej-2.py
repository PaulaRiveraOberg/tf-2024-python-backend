personas = []

while True:
    nombre = input("Ingresa el nombre (o escribe 'FIN' para terminar): ")

    if nombre.upper() == "FIN":
        break

    apellido = input("Ingresa el apellido: ")
    cursos = {}

    curso = input("Ingresa el nombre del curso: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i + 1} para el curso {curso}: "))
        notas.append(nota)

    cursos[curso] = notas
    persona = {"nombre": nombre, "apellido": apellido, "cursos": cursos}
    personas.append(persona)

print("\nLista de personas registradas:")
for persona in personas:
    print(f"\nNombre: {persona['nombre']}, Apellido: {persona['apellido']}")
    print("Cursos inscritos:")
    for curso, notas in persona["cursos"].items():
        promedio = sum(notas) / len(notas)
        print(f"  Curso: {curso}")
        print(f"  Notas: {notas}")
        print(f"  Promedio: {promedio:.2f}")
