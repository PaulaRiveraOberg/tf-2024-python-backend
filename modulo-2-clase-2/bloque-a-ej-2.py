estudiantes = []

for i in range(5):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j + 1} (de 1 a 7) para {nombre}: "))
        notas.append(nota)
    estudiantes.append([nombre, notas])

print("\nPromedio de calificaciones de los estudiantes:")
for estudiante in estudiantes:
    nombre = estudiante[0]
    notas = estudiante[1]
    promedio = sum(notas) / len(notas)  # Calculamos el promedio de las 3 notas
    print(f"Estudiante: {nombre}, Promedio: {promedio:.2f}")
