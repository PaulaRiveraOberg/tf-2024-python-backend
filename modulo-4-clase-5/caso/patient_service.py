import sqlite3
from domain import Patient


def get_patient(patient_id):
    con = sqlite3.connect("tf_backend_api.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM patient WHERE patient_id_pk = ?", (patient_id,)).fetchone()
    if res:
        return Patient(res[0], res[1], res[2]).__dict__()
    else:
        return None


def add_patient(patient):
    con = sqlite3.connect("tf_backend_api.db")
    cur = con.cursor()
    print(patient)
    # try:
    cur.execute("INSERT INTO patient VALUES (?,?,?)", (patient.id, patient.name, patient.current_city,))
    con.commit()
    con.close()
    # except sqlite3.IntegrityError:
    #     print("Patient already exists!!!")
    #     return None
    # finally:
    #     con.close()