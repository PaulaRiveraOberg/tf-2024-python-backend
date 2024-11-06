import pandas as pd

data = {
    'Nombre': ['Ana', 'Maria', 'Sofía', 'Luisa', 'Josefa'],
    'Rut': ['12446500-1', '12181181-2', '11004663-4', '13940675-3', '17027199-8'],
    'Edad': [22, 35, 12, 32, 45],
    'Altura': [1.6, 1.7, 1.6, 1.7, 1.6],
    'Peso': [65, 42, 64, 74, 62]
}
df = pd.DataFrame(data)

# Mostrar el DataFrame
print("DataFrame:")
print(df)

# Describir y discutir los datos
print("\nDescripción del DataFrame:")
print(df.describe())

# Mostrar información del DataFrame
print("\nInformación del DataFrame:")
print(df.info())