import psycopg2
from dotenv import load_dotenv
import os

def connect_db():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn

def create_tables(conn):
    tables = [
        '''-- Crear la tabla 'estudiante'
        CREATE TABLE IF NOT EXISTS estudiante (
            id_estudiante SERIAL PRIMARY KEY,
            rut_estudiante VARCHAR UNIQUE,
            nombre_estudiante VARCHAR NOT NULL,
            fecha_nacimiento DATE NOT NULL,
            direccion VARCHAR,
            correo VARCHAR,
            telefono VARCHAR
        );''',

        '''-- Crear la tabla 'programa'
        CREATE TABLE IF NOT EXISTS programa (
            id_programa SERIAL PRIMARY KEY,
            nombre_programa VARCHAR NOT NULL,
            cantidad_horas INTEGER NOT NULL
        );''',
    ]
    with conn.cursor() as cursor:
        for table in tables:
            cursor.execute(table)
        conn.commit()

def borrar_datos(conn):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM estudiante")
        cursor.execute("DELETE FROM programa")
        conn.commit()

def main():
    load_dotenv()
    conn = connect_db()

    create_tables(conn)
    borrar_datos(conn)

    # paso 1: Inserta al menos 3 registros en la tabla estudiante con datos relevantes como RUT, nombre, dirección y teléfono.
    print("Paso 1: Insertando registros en la tabla estudiante")
    with conn.cursor() as cursor:
        estudiantes = [
            ("12345679-9", "Carlos Lopez", "2000-01-01", "Calle 123", "carlos@example.com", "1234567891"),
            ("12345670-9", "Ana Gomez", "2000-01-01", "Calle 123", "ana@example.com", "1234567892"),
            ("12345671-9", "Pedro Rodriguez", "2000-01-01", "Calle 123", "pedro@example.com", "1234567893"),
        ]
        for estudiante in estudiantes:
            cursor.execute("INSERT INTO estudiante (rut_estudiante, nombre_estudiante, fecha_nacimiento, direccion, correo, telefono) VALUES (%s, %s, %s, %s, %s, %s)", estudiante)
        conn.commit()

    # paso 2: Inserta al menos 2 registros en la tabla programa especificando nombres de programas y su duración en horas.
    print("Paso 2: Insertando registros en la tabla programa")
    with conn.cursor() as cursor:
        programas = [
            ("Programa 1", 100),
            ("Programa 2", 200),
        ]
        for programa in programas:
            cursor.execute("INSERT INTO programa (nombre_programa, cantidad_horas) VALUES (%s, %s)", programa)
        conn.commit()

    # paso 3: Consulta todos los estudiantes que no tienen dirección registrada.
    print("Paso 3: Consultando estudiantes sin dirección")
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM estudiante WHERE direccion IS NULL")
        estudiantes_sin_direccion = cursor.fetchall()
        print(estudiantes_sin_direccion)

    # paso 4: Actualiza la dirección de uno de los estudiantes a un nuevo valor.
    print("Paso 4: Actualizando dirección de un estudiante")
    with conn.cursor() as cursor:
        cursor.execute("UPDATE estudiante SET direccion = 'Calle 456' WHERE id_estudiante = 1")
        conn.commit()

    # paso 5: Elimina un programa específico usando su ID.
    print("Paso 5: Eliminando un programa")
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM programa WHERE id_programa = 1")
        conn.commit()

    # pregunta 1: ¿Cuántos estudiantes tienen direcciones registradas?
    print("Pregunta 1: ¿Cuántos estudiantes tienen direcciones registradas?")
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM estudiante WHERE direccion IS NOT NULL")
        cantidad_estudiantes_con_direccion = cursor.fetchone()[0]
        print(f"Cantidad de estudiantes con direcciones registradas: {cantidad_estudiantes_con_direccion}")

    # pregunta 2: ¿Cuál es la cantidad total de horas entre todos los programas registrados?
    print("Pregunta 2: ¿Cuál es la cantidad total de horas entre todos los programas registrados?")
    with conn.cursor() as cursor:
        cursor.execute("SELECT SUM(cantidad_horas) FROM programa")
        cantidad_horas_totales = cursor.fetchone()[0]
        print(f"Cantidad de horas totales: {cantidad_horas_totales}")

if __name__ == "__main__":
    main()