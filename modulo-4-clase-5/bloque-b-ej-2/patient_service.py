import sqlite3
from domain import Patient


def get_patient(patient_id):
    """
    Obtiene un paciente de la base de datos por su ID.

    Args:
        patient_id (str): Identificador único del paciente a buscar

    Returns:
        dict: Diccionario con los datos del paciente si existe
        None: Si no se encuentra el paciente
    """
    con = sqlite3.connect("tf_backend_api.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM patient WHERE patient_id_pk = ?", (patient_id,)).fetchone()
    if res:
        return Patient(res[0], res[1], res[2]).__dict__()
    else:
        return None


def add_patient(patient):
    """
    Agrega un nuevo paciente a la base de datos.

    Args:
        patient (Patient): Objeto Patient con los datos del paciente a agregar

    Returns:
        None: Si el paciente ya existe o si se agregó exitosamente
    """
    con = sqlite3.connect("tf_backend_api.db")
    cur = con.cursor()

    try:
        cur.execute("INSERT INTO patient VALUES (?,?,?)", (patient.id, patient.name, patient.current_city,))
        con.commit()
    except sqlite3.IntegrityError:
        print("Patient already exists!!!")
        return None
    finally:
        con.close()