import pandas as pd

data = {
    'Nombre': ['Ana', 'Maria', 'Sofía', 'Luisa', 'Josefa'],
    'Rut': ['2446500-1', '12181181-2', '11004663-4', '13940675-3', '17027199-8'],
    'Edad': [22, 35, 12, 32, 45],
    'Altura': [1.6, 1.7, 1.6, 1.7, 1.6],
    'Peso': [65, 42, 64, 74, 62]
}
df = pd.DataFrame(data)

# Crea la columna 'Rut estandarizado'
# sin guión ni digito verificador
# agrega ceros a la derecha si tiene menos de 8 digitos
df['Rut estandarizado'] = df['Rut'].apply(lambda x: x.split('-')[0].replace('.','').zfill(8))

# Crear la columna 'Dígito verificador'
df['Digito verificador'] = df['Rut'].apply(lambda x: x.split('-')[1])

# Calcular el Índice de Masa Corporal (IMC)
df['IMC'] = df['Peso'] / (df['Altura'] ** 2)

# Crear la columna 'Clasificación de edad'
def clasificar_edad(edad):
    if edad > 60:
        return 'Mayor de 60 años'
    elif edad > 30:
        return 'Mayor de 30 años'
    else:
        return 'Menor de 30 años'

df['Clasificación de edad'] = df['Edad'].apply(clasificar_edad)

# Mostrar el DataFrame resultante
print("DataFrame con nuevas columnas:")
print(df)