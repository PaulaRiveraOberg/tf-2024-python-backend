import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo titanic.csv en un DataFrame
df = pd.read_csv('modulo-2-clase-7/titanic.csv')

# transformaciones de datos
df['Sexo'] = df['Sex'].map({'male': 'masculino', 'female': 'femenino'})
def categorize_age(age: float) -> str:
    if age < 18:
        return 'menor'
    elif 18 <= age < 60:
        return 'adulto'
    else:
        return 'adulto mayor'
df['AgeGroup'] = df['Age'].apply(categorize_age)

plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.barplot(data=df, x='AgeGroup', y='Survived', palette='viridis', hue='AgeGroup', errorbar=None)
plt.title('Tasa de Supervivencia por Grupo de Edad')
plt.xlabel('Grupo de Edad')
plt.ylabel('Tasa de Supervivencia (%)')
plt.xticks(rotation=45)
# mostrar como %
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y * 100:.0f}%'))
# plt.show()
# guarda como imagen
plt.savefig('modulo-2-clase-7/img/tasa_supervivencia_grupo_edad.png')

# Distribución del Precio del Pasaje por Supervivencia
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
# orient='h' cambia la orientación del gráfico boxplot
sns.boxplot(data=df, x='Fare', y='Survived', palette='viridis', hue='Survived', orient='h')
plt.title('Distribución de Tarifa Pasaje por Supervivencia')
plt.ylabel('Supervivencia')
plt.xlabel('Tarifa Pasaje')
# Limitar el eje x de 0 a 300
plt.xlim(0, 300)
plt.yticks([0, 1], ['No Sobrevivió', 'Sobrevivió'])
# plt.show()
plt.savefig('modulo-2-clase-7/img/distribucion_tarifa_pasaje_supervivencia.png')
