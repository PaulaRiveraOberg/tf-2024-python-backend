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

        '''-- Crear la tabla 'curso'
        CREATE TABLE IF NOT EXISTS curso (
            id_curso SERIAL PRIMARY KEY,
            codigo_curso VARCHAR UNIQUE NOT NULL,
            cantidad_estudiantes INTEGER NOT NULL,
            fecha_inicio DATE NOT NULL,
            fecha_termino DATE NOT NULL,
            id_programa INTEGER NOT NULL,
            FOREIGN KEY (id_programa) REFERENCES programa(id_programa)
        );''',

        '''-- Crear la tabla 'estudiante_curso' (relación muchos a muchos entre estudiante y curso)
        CREATE TABLE IF NOT EXISTS estudiante_curso (
            id_estudiante INTEGER NOT NULL,
            id_curso INTEGER NOT NULL,
            PRIMARY KEY (id_estudiante, id_curso),
            FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante) ON DELETE CASCADE,
            FOREIGN KEY (id_curso) REFERENCES curso(id_curso) ON DELETE CASCADE
        );''',
    ]
    with conn.cursor() as cursor:
        for table in tables:
            cursor.execute(table)
        conn.commit()

def borrar_datos(conn):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM estudiante_curso")
        cursor.execute("DELETE FROM curso")
        cursor.execute("DELETE FROM programa")
        cursor.execute("DELETE FROM estudiante")
        conn.commit()

def main():
    load_dotenv()
    conn = connect_db()

    create_tables(conn)
    # borrar_datos(conn)

    try:
        with conn.cursor() as cursor:
            # paso 1: Insertar un nuevo estudiante en la tabla estudiante. Considere almacenar los datos del nuevo estudiante en variables separadas.
            print("Paso 1: Insertar datos en la tabla estudiante")
            estudiante = (
                "12345678-9",
                "Juan Perez",
                "2000-01-01",
                "Calle 123",
                "juan@example.com",
                "1234567890"
            )
            # insert and return id
            cursor.execute("INSERT INTO estudiante (rut_estudiante, nombre_estudiante, fecha_nacimiento, direccion, correo, telefono) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_estudiante", estudiante)
            id_estudiante = cursor.fetchone()[0]

            # paso 2: Verificar si un programa especifico existe en la tabla programa.
            print("Paso 2: Verificar si un programa especifico existe en la tabla programa")
            cursor.execute("SELECT id_programa FROM programa WHERE nombre_programa = 'Programa 1'")
            id_programa = cursor.fetchone()[0]
            if id_programa:
                print("El programa existe")
            else:
                print("El programa no existe")
                raise Exception("El programa no existe")

            # paso 3: Si el programa existe, registrar la inscripción del estudiante en la tabla curso.
            print("Paso 3: Registrar la inscripción del estudiante en la tabla curso")
            cursor.execute('''INSERT INTO curso (codigo_curso, cantidad_estudiantes, fecha_inicio, fecha_termino, id_programa) 
                        VALUES ('1234567890', 1, '2025-01-01', '2025-01-01', %s) RETURNING id_curso''', (id_programa,))
            id_curso = cursor.fetchone()[0]
            cursor.execute('''INSERT INTO estudiante_curso (id_estudiante, id_curso) VALUES (%s, %s)''', (id_estudiante, id_curso))
            
            # paso 4: Confirmar los cambios con commit.
            conn.commit()
            print("Transacción exitosa")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        conn.close()


if __name__ == "__main__":
    main()