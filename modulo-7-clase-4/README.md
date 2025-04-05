# Modulo 7: Patrones de Integración e Interoperabilidad en entornos Python

## Clase 4: Mensajería

### Dependencias

Primero debemos instalar las dependencias necesarias en nuestro entorno virtual:

```bash
pip install pika
```

También debemos instalar el servidor de RabbitMQ. Este lo podemos instalar con chocolatey en windows:

```bash
choco install rabbitmq
```

En OSX podemos instalar con homebrew:

```bash
brew install rabbitmq
```

En Linux, podemos instalar con apt:

```bash
sudo apt install rabbitmq-server
```

El instalador e instrucciones para instalar en windows, OSX y Linux, pueden encontrarse en [el sitio de RabbitMQ](https://www.rabbitmq.com/download.html).

### RabbitMQ CLI

RabbitMQ nos proporciona una herramienta CLI para interactuar con el servidor. Esta se instala con el instalador de RabbitMQ.

Algunos comandos útiles:

```bash
# consultar el estado del servidor
rabbitmqctl status

# ayuda
rabbitmqctl help

# agregar un usuario
rabbitmqctl add_user <username> <password>

# eliminar un usuario
rabbitmqctl delete_user <username>

# crear un entorno virtual
rabbitmqctl add_vhost <vhost>

# eliminar un entorno virtual
rabbitmqctl delete_vhost <vhost>

# agregar permisos a un usuario para un entorno virtual
rabbitmqctl set_permissions -p <vhost> <username> ".*" ".*" ".*"
```

### Producer

El producer es el encargado de enviar mensajes a la cola. Archivos:

- `producer.py`: Producer que envía mensajes a la cola.

### Consumer

El consumer es el encargado de recibir mensajes de la cola. Archivos:

- `consumer.py`: Consumer que recibe mensajes de la cola.

Para probar el ejemplo debemos seguir los siguientes pasos:

1. Iniciar el servidor de RabbitMQ.
2. Ejecutar el consumer.
    ```bash
    python consumer.py
    ```
3. Ejecutar el producer.
    ```bash
    python producer.py
    ```
4. Verificar que el mensaje se ha enviado y recibido correctamente.

### Trabajo Grupal Bloque A

Entendiendo la mensajería

- Instale RabbitMQ (en Windows se sugiere con instalador; en Linux y Mac se sugiere con
Docker).
- Utilice el código entregado (“hello world”) para entender la mensajería.
- Mantenga dos receptores: ¿qué ocurre?
- Discuta con su equipo cómo se podría implementar una operación distribuida con lo que
hemos visto hasta ahora.
    - Implemente una operación “staged” y detenga el envío de mensajes.
    - Observe y discuta la asincronía: el productor no necesita estar arriba esperando la respuesta del receptor.

### Trabajo Grupal Bloque B

Entendiendo la mensajería

- Ejecute los dos códigos.
- Modifíquelos enviando distintos mensajes para que usted y su equipo puedan discutir la mensajería subyacente.
- Cree varias instancias de trabajadores y suscriptores. Observe el comportamiento.
- En particular, en los trabajadores asigne un mecanismo de “delay” entre que se recibe el trabajo y se realiza el “ack”.
- Escoja un tiempo apropiado de tal forma que pueda detener el trabajador y ver lo que pasa con el trabajo pendiente.