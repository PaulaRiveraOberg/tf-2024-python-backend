# Modulo 5 - Clase 7

## Setup

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Carga de datos

Puede cargar los datos de prueba con el siguiente comando:

```bash
python manage.py shell < ../populate_db.py
# en powershell
(Get-Content ../populate_db.py) | python ./manage.py shell
```