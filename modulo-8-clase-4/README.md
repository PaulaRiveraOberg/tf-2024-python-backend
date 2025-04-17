# Modulo 8: Fundamentos de Integración Continua

## Clase 3: Docker y Containers

### Parte 1: Instalación de Docker

Instalamos Docker Desktop en [https://docs.docker.com/get-started/introduction/get-docker-desktop/](https://docs.docker.com/get-started/introduction/get-docker-desktop/)

Para instalar Docker en Windows también podemos usar Chocolatey.

```bash
choco install docker-desktop
```

### Parte 2: Crear un contenedor Docker para el proyecto

Nos basaremos en un proyecto de ejemplo disponible en el directorio [miproyecto](./miproyecto).

Lo primero que debemos hacer crear un archivo Dockerfile en la raiz del proyecto, en este caso en la carpeta [miproyecto](./miproyecto).

```Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

Para construir la imagen, ejecutamos el siguiente comando en la raiz del proyecto.

```bash
docker build -t django-app .
```

Podemos revisar las imágenes que tenemos en nuestro equipo con el siguiente comando.

```bash
docker images
```

Debieramos ver en el listado una imagen con el nombre `django-app`.


Para ejecutar el contenedor, ejecutamos el siguiente comando.

```bash
docker run -p 8000:8000 django-app
```

Para detener el contenedor apretamos `Ctrl + C`.

Si queremos correr un comando distinto al definido en el Dockerfile, podemos hacerlo con el siguiente comando.

```bash
docker run -p 8000:8000 django-app python manage.py migrate
```

Si queremos ingresar de modo interactivo al contenedor, podemos hacerlo con el siguiente comando.

```bash
docker run -it django-app bash
```

Si hacemos cambios en el código, podemos volver a construir la imagen y ejecutar el contenedor nuevamente.

```bash
docker build -t django-app .
docker run -p 8000:8000 django-app
```

### Parte 3: Utilizacieon de Docker Compose

Docker Compose es una herramienta que nos permite definir y ejecutar aplicaciones Docker de forma más sencilla.

Docker compose se instala como parte de Docker Desktop.

Para trabajar con Docker Compose, debemos crear un archivo `docker-compose.yml` en la raiz del proyecto. Este archivo sigue la sintaxis de YAML y en el definimos los servicios que vamos a utilizar.

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    env_file:
      - .env
    command: python manage.py runserver 0.0.0.0:8000
```

Para iniciar el contenedor, ejecutamos el siguiente comando.

```bash
docker-compose up
```

Si ejecutamos el comando por primera vez, Docker Compose va a construir la imagen y a iniciar el contenedor.

Si queremos volver a contruir la imagen debemos ejecutar el siguiente comando.

```bash
docker-compose build
```

Si queremos iniciar el contenedor nuevamente, ejecutamos el siguiente comando.

```bash
docker-compose up
```

Si lo queremos iniciar en segundo plano, ejecutamos el siguiente comando.

```bash
docker-compose up -d
```

Podemos ejecutar un comando específico para un servicio con el siguiente comando, en este caso hemos llamado al servicio `web` que es el nombre del servicio que definimos en el archivo `docker-compose.yml`.

```bash
docker-compose run web python manage.py migrate
```

Si queremos ingresar de modo interactivo al contenedor que se encuentra en ejecución, podemos hacerlo con el siguiente comando.

```bash
docker-compose exec web bash
```

Si queremos ejecutar un comando en modo interactico podemos usar el siguiente comando.

```bash
docker-compose run web python manage.py shell
```

Si queremos detener el contenedor que se encuentra en ejecución en segundo plano, ejecutamos el siguiente comando.

```bash
docker-compose down
```

