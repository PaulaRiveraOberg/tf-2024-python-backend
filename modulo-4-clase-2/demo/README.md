## Primeros pasos

### Creación de entorno virtual

Antes de trabajar en un proyecto particular es recomendable crear un entorno virtual para trabajar con python. En el curso vamos a usar [venv](https://docs.python.org/es/3/library/venv.html) para crear un entorno virtual, este comando creará un directorio llamado `.venv` que contendrá el entorno virtual:

```bash
python -m venv .venv
```

Luego de crear el entorno virtual es necesario activarlo, en linux y mac se puede activar con el siguiente comando:

```bash
source .venv/bin/activate
```

en el caso de windows se puede activar con el siguiente comando:

```bash
.venv\Scripts\activate
```

Tanto en vscode como en pycharm es necesario configurar el interprete de python para que use el entorno virtual, en vscode esto se hace en el archivo `.vscode/settings.json` y en pycharm esto se hace en el archivo `settings.json` que se encuentra en la carpeta del proyecto. O a traves de la preferencia de la IDE.
* [VSCode](https://code.visualstudio.com/docs/python/environments#_selecting-and-using-an-environment)
* [PyCharm](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)

### Instalación de Django

Para instalar django se puede usar el siguiente comando:

```bash
pip install django
```

para verificar que django está correctamente instalado se puede usar el siguiente comando:

```bash
django-admin --version
``` 

### Creación de un proyecto y una aplicación

Una vez instalado django se puede crear un nuevo proyecto con el siguiente comando:

```bash
django-admin startproject demo
```

Vamos a crear una aplicación llamada `avisos`, para esto usamos el comando `startapp`:

```bash
django-admin startapp myapp
```

Debemos agregar la aplicación al proyecto, para esto debemos modificar el archivo `demo/settings.py` y agregar `myapp.apps.MyappConfig` en la lista `INSTALLED_APPS`.

Para iniciar el servidor de desarrollo usamos el comando `runserver`:

```bash
python manage.py runserver
```