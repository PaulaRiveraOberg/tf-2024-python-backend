# Modulo 8: Fundamentos de Integración Continua

## Clase 3: Continuos Deployment

Crear un Pipeline CI en GitHub Actions para un Proyecto Python/Django con despliege automatico a render.com y utilización de base de datos PostgreSQL en neon.tech.

### Parte 1: Preparar tu proyecto

Nos basaremos en un proyecto de ejemplo disponible en el repositorio [django-drf-cicd-example](https://github.com/rarce/django-drf-cicd-example). Para trabajar lo primero que haremos será hacer un fork del repositorio. Luego vamos a clonar el nuevo repositorio creado en nuestro equipo.

```bash
git clone https://github.com/tu-usuario/django-drf-cicd-example.git
```

Luego vamos a crear el ambiente virtual e instalar las dependencias del proyecto.

```bash
# cambiar a la carpeta del proyecto
cd django-drf-cicd-example
# crear y activar el ambiente virtual
python -m venv venv
# activar el ambiente virtual en windows
./venv/Scripts/activate
# para activar el ambiente virtual en linux/osx
source venv/bin/activate
# instalar las dependencias
pip install -r requirements.txt
```

Luego vamos a crear el archivo .env desde el archivo .env.example y agregar las variables de entorno.

```bash
# crear el archivo .env
cp .env.example .env
```

Requerimos las siguientes variables de entorno:
* `PGDATABASE`
* `PGUSER`
* `PGPASSWORD`
* `PGHOST`
* `PGPORT`
* `SECRET_KEY`
* `PRODUCTION_HOST`
* `DEBUG`

De momento solo podemos configurar las variables `DEBUG=true` y `SECRET_KEY`. Ya que para las otras variables necesitamos una cuenta en Render y Neon.

Vamos a probar el proyecto localmente para verificar que todo esté funcionando correctamente. Para esto vamos a modificar el archivo settings que se utiliza de modo que localmente utizará un bd sqlite.

```bash
# correremos las migraciones
python manage.py migrate --settings=myproject.settings_dev
# iniciamos el servidor
python manage.py runserver --settings=myproject.settings_dev
```

Si todo está bien, deberíamos poder acceder a la aplicación en http://localhost:8000

### Creacion de cuentas

La manera más simple de crear cuentas en Render y Neon es hacerlo con una cuenta de Google o GitHub.

- [Render](https://dashboard.render.com/register)
- [Neon](https://console.neon.tech/signup)

### Creación de BD en Neon

Al ingresar a Neon por primera vez nos pedirá crear un projecto. Podemos elegir el nombre del proyecto y la región, además de la ultima versión de Postgres.

![Crear proyecto en Neon](./images/neon-create-project.png)

Desde el dashboard de Neon podemos ver los detalles de nuestro proyecto, las tablas, queries, etc. Daremos click en "Connect" para obtener las credenciales de la base de datos.

![Dashboard de Neon](./images/neon-dashboard.png)

![Credenciales de Neon](./images/neon-credentials.png)

Debemos guardar el string de conexión para utilizarlo en nuestro proyecto.

Neon nos proporciona un string de conexión para utilizarlo en nuestro proyecto. Este string se ve así:

```bash
postgresql://user:password@host:port/database?sslmode=require
```

Desde este completaremos los valores de las variables de entorno de nuestro archivo .env. Por ejemplo:
* `PGDATABASE`: database
* `PGUSER`: user
* `PGPASSWORD`: password
* `PGHOST`: host
* `PGPORT`: port

### Creación de proyecto en Render

Tras crear una cuenta en Render, desde el dashboard podemos crear un nuevo proyecto, debemos crear uno de tipo "Web Services".

![Crear proyecto en Render](./images/render-create-project.png)

Conectar el proyecto con GitHub.

![Conectar con GitHub](./images/render-connect-github.png)

En github puedes entregar acceso especifico al repositorio que render necesita.

![Acceso a repositorio](./images/render-github-access.png)

Ahora debemos configurar el entorno de render.

![Configurar entorno](./images/render-configure-environment.png)

Debemos asegurarnos de elegir lo siguiente:
* Lenguaje: Python
* Branch: main
* Región: US East
* Build Command: `./build.sh`
* Start Command: `python -m gunicorn myproject.asgi:application -k uvicorn.workers.UvicornWorker`
* Instance Type: Free

Luego en variables de entorno debemos agregar las siguientes variables:

![Configurar variables de entorno](./images/render-configure-environment-variables.png)

* `SECRET_KEY`: clave secreta para el proyecto, podemos generar una con `python -c 'import secrets; print(secrets.token_hex(32))'`
* `PGDATABASE` valor desde neon
* `PGUSER` valor desde neon
* `PGPASSWORD` valor desde neon
* `PGHOST` valor desde neon
* `PGPORT` valor desde neon
* `PRODUCTION_HOST` lo dejaremos como example.com de momento ya que necesitamos que render nos asigne el dominio.

Una vez configurado todo, podemos hacer click en el botón "Deploy" para iniciar el despliegue.

Cuando el despliegue termine, podemos ver el dominio asignado en el dashboard de Render. Debemos editar nuevamente el entorno en Render, para esto vamos a Manage > Environment, y desde aquí damos en "Edit" en la sección "Environment Variables" y completamos el valor de `PRODUCTION_HOST` con el dominio asignado.



