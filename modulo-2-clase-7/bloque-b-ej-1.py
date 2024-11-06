import pandas as pd

# Cargar el archivo titanic.csv en un DataFrame
df = pd.read_csv('modulo-2-clase-7/titanic.csv')

# Mostrar las primeras filas del DataFrame para entender su estructura
print("Primeras 5 filas del DataFrame:")
print(df.head())

# Describir y discutir los metadatos del DataFrame
print("\nInformación general del DataFrame:")
print(df.info())

print("\nDescripción estadística del DataFrame:")
print(df.describe(include='all'))