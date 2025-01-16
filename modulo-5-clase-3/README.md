## Clase 3: Acceso a Datos con SQL Nativo en Python

### Requisitos

Instalación de psycopg2 

Para instalar psycopg2, se puede usar el siguiente comando:

```bash
pip install psycopg2-binary
```

Instalamos el paquete `psycopg2-binary` que es una versión binaria de psycopg2, es decir, que no necesita compilar psycopg2.

Para conectarse a una base de datos PostgreSQL, se puede usar el siguiente código:

```python
import psycopg2
# Conectar a la base de datos
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myusername",
    password="mypassword"
)
cursor = conn.cursor()
# Ejecutar una consulta
cursor.execute("SELECT * FROM mytable")
result = cursor.fetchall()
print(result)
# Cerrar el cursor y la conexión
cursor.close()
conn.close()
```

Una practica comun para guardar secretos es usar variables de entorno, podemos usar el paquete `python-dotenv` para cargar las variables de entorno desde un archivo `.env`.

Para guardar los datos de conexión crearemos un archivo `.env` con las siguientes variables, este archivo no está versionado por lo que no se debe subir a GitHub, se debe agregar a `.gitignore` y solo dejamos disponible un `.env.example` que se puede copiar y renombrar a `.env`:

```bash
DB_HOST=localhost
DB_NAME=modulo-5-clase-3
DB_USER=postgres
DB_PASSWORD=postgres
```

Para cargar las variables de entorno usaremos el paquete `python-dotenv`.

```bash
pip install python-dotenv
```

## Ejercicio A: Implementando consultas básicas con psycopg2

Usando el esquema del script SQL proporcionado, interactúe con las tablas estudiante y programa.

### Tareas a realizar:

    1. Paso 1: Inserta al menos 3 registros en la tabla estudiante con datos relevantes como RUT, nombre, dirección y teléfono.
    2. Paso 2: Inserta al menos 2 registros en la tabla programa especificando nombres de programas y su duración en horas.
    3. Paso 3: Consulta todos los estudiantes que no tienen dirección registrada.
    4. Paso 4: Actualiza la dirección de uno de los estudiantes a un nuevo valor.
    5. Paso 5: Elimina un programa específico usando su ID.

### Muestre por pantalla:
    1. ¿Cuántos estudiantes tienen direcciones registradas?
    2. ¿Cuál es la cantidad total de horas entre todos los programas registrados?

## Solución

* [solución](ejercicio-bloque-a.py)

## Ejercicio B: Manejo de transacciones con try-except, commit y rollback.

Basados en el resultado del ejercicio anterior.

1. Crear un script en Python que siga el siguiente flujo:
    a) Insertar un nuevo estudiante en la tabla estudiante. Considere almacenar los datos del nuevo estudiante en variables separadas. 
    b) Verificar si un programa especifico existe en la tabla programa.
    c) Si el programa existe, registrar la inscripción del estudiante en la tabla `estudiante_curso` para el curso asociado al programa anterior.
    d) Confirmar los cambios con commit.
    e) En caso de error, usar rollback para revertir los cambios.
2. Condiciones:
    a) Si el id_programa no existe, generar un error y revertir la transacción.
    b) Manejar excepciones, recuerde clase 5 del modulo 2 de este curso. 

## Solución

* [solución](ejercicio-bloque-b.sql)

