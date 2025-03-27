## Modulo 7: Patrones de Integración e Interoperabilidad en entornos Python

## Clase 1: Llamado a procedimientos remotos

## Uso de gRPC

gRPC es un framework de RPC (Remote Procedure Call) que permite a las aplicaciones comunicarse entre sí a través de una red. 

Instalación de dependencias:

```bash
pip install grpcio
pip install grpcio-tools
```

El archivo `distance_unary.proto` se encuentra en el directorio `modulo-7-clase-1`, este contiene el servicio `DistanceService` con el procedimiento remoto `geodesic_distance`. Para generar los archivos de Python, se debe ejecutar el siguiente comando:

```bash
python -m grpc_tools.protoc -I./ --python_out=. --pyi_out=. --grpc_python_out=. ./distance_unary.proto
```

El comando anterior generará los archivos `distance_unary_pb2.py` y `distance_unary_pb2_grpc.py` en el directorio `modulo-7-clase-1`.

### Ejecución del servidor

Para ejecutar el servidor, se debe ejecutar el siguiente comando:

```bash
python server.py
```

### Ejecución del cliente

Para ejecutar el cliente, se debe ejecutar el siguiente comando:

```bash
python client.py
```

## Ejercicio Bloque A

### Parte 1

* Comprenda el código, ejecute algunas modificaciones menores para entender el funcionamiento del mismo.
* Compile los protocol buffers entregados con pequeños cambios.

### Parte 2

* Modifique el código cliente para el cálculo de una serie de posiciones (más de 10) de tal manera que pueda determinar la distancia recorrida en total en un camino.
* Puede inventar posiciones cercanas, pero sería ideal que las busque en un software como Google Earth o Google Maps para obtener valores reales.
* Discuta con su equipo la rapidez de un backend construido con gRPC.