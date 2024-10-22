nudos_a_kmh = lambda nudos: nudos * 1.852

estacion = input("Ingrese el nombre de la estación de monitoreo: ")

vientos_nudos = {
    "5 horas": float(input("Ingrese el viento registrado en nudos hace 5 horas: ")),
    "10 horas": float(input("Ingrese el viento registrado en nudos hace 10 horas: ")),
    "15 horas": float(input("Ingrese el viento registrado en nudos hace 15 horas: ")),
}

vientos_kmh = dict(
    map(lambda key: (key, nudos_a_kmh(vientos_nudos[key])), vientos_nudos.keys())
)

print(f"Estación: {estacion}")
print("Vientos registrados en km/h:")
for hora, velocidad in vientos_kmh.items():
    print(f"En las últimas {hora}: {velocidad:.2f} km/h")
