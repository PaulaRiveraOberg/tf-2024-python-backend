# Ejercicio A

Para instalar las dependencias, ejecutar:

```bash
pip install django django-rest-framework
```

Luego se deben correr las migraciones:

```bash
python manage.py migrate
```

Podemos cargar datos de usuarios y libros de prueba mediante el siguiente comando:

```bash
python manage.py loaddata books/seed/users.json
python manage.py loaddata books/seed/books.json
```

* El usuario admin tiene username `admin` y password `admin`.
* El usuario user tiene username `user` y password `user`.

Luego, se debe ejecutar el servidor:

```bash
python manage.py runserver
```

Podemos probar los endpoints de la API mediante el siguiente comando:

* Lista de librossin autenticación:
```bash
curl -X GET http://localhost:8000/api/biblioteca/
```

* Lista de libros con autenticación http basic auth:
```bash
curl -X GET http://localhost:8000/api/biblioteca/ -u user:user
```

* Lista de libros con autenticación http basic auth:
```bash
curl -X GET http://localhost:8000/api/biblioteca/ -u admin:admin
```

* Lista de libros VIP con autenticación http basic auth, retorno de error:
```bash
curl -X GET http://localhost:8000/api/sala-vip/ -u user:user
```

* Lista de libros VIP con autenticación http basic auth:
```bash
curl -X GET http://localhost:8000/api/sala-vip/ -u admin:admin
```








