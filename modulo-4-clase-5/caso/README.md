## Caso REST con FastAPI

### Requerimientos

* Implementaremos un servicio `Paciente` para una clínica.
* El servicio es `stand-alone`, es decir, similar a un microservicio.
* Utiliza una base de datos sqlite.
* Provee endpoints para Pacientes y Exámenes.

### Estructura del servicio

* Archivo models.py contiene todos nuestros modelos.
* Archivos `*_service.py`: contienen los servicios de storage (comunicación con la base de datos).
* Archivo `request_handler.py` implementa los endpoints.
* Archivo `domain.py` contiene las clases del dominio (distintas a las clases de modelos).
* Archivo `tf_backend_api.db` contiene la base de datos sqlite.


### Implementación

Para implementar el servicio primero implementaremos la clase `Patient` en el archivo `domain.py`. 

```python
class Patient:
    def __init__(self, id, name, current_city):
        self.id = id
        self.name = name
        self.current_city = current_city

    def __dict__(self):
        return {
            "patient_id": self.id,
            "name": self.name,
            "current_city": self.current_city
        }
```

Este archivo contiene el constructor de la clase `Patient` y el método `__dict__` que convierte el objeto `Patient` a un diccionario para que pueda ser serializado a JSON por FastAPI.


Con esta clase ya definida, podemos implementar los servicios de almacenamiento en la base de datos en el archivo `patient_service.py`.

```python
import sqlite3
from domain import Patient

def get_patient(patient_id):
    con = sqlite3.connect("tf_backend_api.db")
    with con.cursor() as cur:
        res = cur.execute("SELECT * FROM patient WHERE patient_id_pk = ?", (patient_id,)).fetchone()
        if res:
            return Patient(res[0], res[1], res[2]).__dict__()
        else:
            return None


def add_patient(patient):
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
```

El servicio de almacenamiento contiene las funciones `get_patient` y `add_patient` que permiten obtener y agregar pacientes a la base de datos.

Para definir los endpoint requeriremos definir en el archivo `models.py` el modelo `PatientModel` que contiene los campos del paciente, para la creación de pacientes.

```python
from pydantic import BaseModel

class PatientModel(BaseModel):
    id: str
    name: str
    current_city: str
```

Con este modelo ya definido, podemos implementar los endpoints en el archivo `request_handler.py`.

```python
from fastapi import FastAPI, HTTPException
import patient_service
from models import PatientModel
app = FastAPI()


@app.get("/patient/{patient_id}")
def patient_details(patient_id: str):
    result = patient_service.get_patient(patient_id)
    return result

@app.post("/patient")
def add_patient(patient: PatientModel):
    result = patient_service.add_patient(patient)
    if not result:
        raise HTTPException(status_code=400, detail="Patient already exists!")
    else:
        return result
```

### Ejecución

Para ejecutar el servicio, se debe correr el archivo `request_handler.py` con el comando:

```bash
uvicorn request_handler:app --host 0.0.0.0 --port 8000 --reload
```

Prueba de endpoint de obtener paciente:

```bash
curl http://localhost:8000/patient/6889998-3
```

Prueba de endpoint de agregar paciente usando curl:

```bash
curl -X POST "http://localhost:8000/patient" -H "Content-Type: application/json" -d '{"id": "1-6", "name": "Juan Perez", "current_city": "Santiago"}'
```

Revisar en la base de datos que se haya agregado el paciente.

```bash
curl http://localhost:8000/patient/1-6
```
