from fastapi import FastAPI, HTTPException
import patient_service
from models import PatientModel
app = FastAPI()


@app.get("/patient/{patient_id}")
def patient_details(patient_id: str):
    """
    Endpoint para obtener los detalles de un paciente por su ID.

    Args:
        patient_id (str): Identificador único del paciente a buscar

    Returns:
        dict: Diccionario con los datos del paciente si existe
        None: Si no se encuentra el paciente
    """
    result = patient_service.get_patient(patient_id)
    return result


@app.post("/patient")
def add_patient(patient: PatientModel):
    """
    Endpoint para agregar un nuevo paciente al sistema.

    Args:
        patient (PatientModel): Modelo con los datos del paciente a agregar

    Returns:
        dict: Datos del paciente agregado si la operación fue exitosa

    Raises:
        HTTPException: Si el paciente ya existe en el sistema (código 400)
    """
    result = patient_service.add_patient(patient)
    if not result:
        raise HTTPException(status_code=400, detail="Patient already exists!")
    else:
        return result