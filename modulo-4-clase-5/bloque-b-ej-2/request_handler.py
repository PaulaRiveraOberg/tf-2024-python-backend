from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import HTMLResponse
import patient_service
from models import PatientModel
app = FastAPI()


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
    

@app.get("/patient/{patient_id}", response_class=HTMLResponse)
def patient_details(patient_id: str):
    result = patient_service.get_patient(patient_id)
    if result:
        html = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>Detalles del Paciente</title>
            </head>
            <body>
                <h1>Detalles del Paciente</h1>
                <p>ID: {result['patient_id']}</p>
                <p>Nombre: {result['name']}</p>
                <p>Ciudad: {result['current_city']}</p>
                <p><a href="/patient/{result['patient_id']}/xml">Ver en formato XML</a></p>
            </body>
        </html>
        """
        return HTMLResponse(content=html)
    else:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")

@app.get("/patient/{patient_id}/xml")
def patient_details_xml(patient_id: str):
    result = patient_service.get_patient(patient_id)
    if result:
        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<patient>
    <id>{result['patient_id']}</id>
    <name>{result['name']}</name>
    <city>{result['current_city']}</city>
</patient>"""
        return Response(content=xml, media_type="application/xml")
    else:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")