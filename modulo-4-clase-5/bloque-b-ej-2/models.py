from pydantic import BaseModel

class PatientModel(BaseModel):
    """
    Modelo de datos para representar un paciente en el sistema.
    
    Attributes:
        id (str): Identificador único del paciente
        name (str): Nombre completo del paciente
        current_city (str): Ciudad actual de residencia del paciente
    """
    id: str
    name: str
    current_city: str