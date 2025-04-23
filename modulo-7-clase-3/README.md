# ## Modulo 7: Patrones de Integración e Interoperabilidad en entornos Python

## Clase 3: Adaptadores

### Dependencias

Primero debemos instalar las dependencias necesarias en nuestro entorno virtual:

```bash
pip install grpcio grpcio-tools requests fastapi uvicorn
```

### Patron Adapter

En este ejemplo se muestra la utilización del patrón Adapter para integrar un servicio externo. Archivos:

- `patient_adapter.py`: Implementación del patrón Adapter.
- `patient_client.py`: Cliente que solicita la información del paciente.
- `patient_adapter_unary.proto`: Definición del servicio RPC.
- `patient_service_external.py`: Servicio externo que proporciona la información del paciente.

Generación de los stubs:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. patient_adapter_unary.proto
```

### Ejecución:

Se debe ejecutar el servicio externo en un terminal:

```bash
uvicorn patient_service_external:app --reload
```

Luego, en otro terminal, se debe ejecutar el adaptador:

```bash
python patient_adapter.py
```

Finalmente, se debe ejecutar el cliente:

```bash
python patient_client.py
```

El flujo es el siguiente:

1. El cliente hace una solicitud gRPC al servidor
2. El servidor obtiene datos de un servicio HTTP externo
3. Los datos se adaptan del formato remoto al formato local
4. La información adaptada se devuelve al cliente

### Ejercicio

Mejorando el adaptador

* Incorpore un listado de exámenes a cada paciente (separados por “-”, luego de haber sido separados por “;”).
* Modifique el adaptador (el código que sea necesario) para realizar una adaptación adecuada de forma que el cliente pueda “entender” a un paciente con sus exámenes en formato “JSON”.
