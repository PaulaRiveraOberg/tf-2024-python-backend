# ## Modulo 7: Patrones de Integración e Interoperabilidad en entornos Python

## Clase 2: Transacciones de Larga Duración

### Dependencias

Primero debemos instalar las dependencias necesarias en nuestro entorno virtual:

```bash
pip install grpcio
pip install grpcio-tools
```

### Patron SAGA

El sistema a continuación implementa un patrón SAGA síncrono usando gRPC:

El sistema consta de dos *servicios principales*:
 * `CourseService`: Maneja la gestión de cursos, en archivo `course_service.py`
 * `DeliveryService`: Maneja la entrega de cursos, en archivo `delivery_service.py`

 La *defición de los servicios* se encuentra en los archivos:
  * `course_service.proto`: Define el servicio de gestión de cursos
  * `delivery_service.proto`: Define el servicio de entrega de cursos

Para generar los archivos de definición de servicios, ejecutamos:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. course_service.proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. delivery_service.proto
```

Componentes principales del sistema:
 * `transaction_orchestrator.py`: Orquestador de la transacción
    * Actúa como el coordinador principal de la transacción
    * Inicia el SAGA y maneja la lógica de compensación si falla
 * `client.py`: Cliente que ejecuta la transacción
    * Implementa la lógica principal del SAGA
    * Contiene dos funciones principales:
        * `course_saga()`: Ejecuta la transacción principal
        * `saga_compensating_transaction()`: Maneja la compensación si falla
 
 #### Flujo de la transacción

 * Transacción Principal (course_saga()):
    * Primero intenta entregar el curso (DeliveryService)
    * Luego intenta agregar el curso (CourseService)
    * Si cualquiera falla (código de estado diferente a 10), marca la transacción como fallida
 * Transacción de Compensación (saga_compensating_transaction()):
    * Se ejecuta solo si la transacción principal falla
    * Deshace las operaciones en orden inverso:
        * Primero remueve el curso (CourseService)
        * Luego desentrega el curso (DeliveryService)

#### Ejecución

Para ejecutar el sistema, ejecutamos primero los servicios, cada uno en una terminal:

```bash
python course_service.py
python delivery_service.py
```

Luego, ejecutamos el orquestador:

```bash
python transaction_orchestrator.py
```