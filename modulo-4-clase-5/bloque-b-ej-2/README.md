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

### Servidor

Para ejecutar el servidor, se puede usar el siguiente comando:

```
uvicorn request_handler:app --host 0.0.0.0 --port 8000 --reload
```

### Implementación

Se implementa un endpoint GET para obtener los datos de un paciente en el archivo `request_handler.py`. Para probar el endpoint, se puede usar la siguiente URL:

```
http://localhost:8000/patient/6889998-3
```

