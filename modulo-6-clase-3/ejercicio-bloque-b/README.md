# Ejercicio A

Para instalar las dependencias, ejecutar:

```bash
pip install django django-rest-framework djangorestframework-simplejwt
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

Primero debemos obtener el token de acceso:

```bash
curl http://localhost:8000/api/token/ -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}'
```

Luego, podemos probar los endpoints de la API mediante el siguiente comando:
Podemos probar los endpoints de la API mediante el siguiente comando:

* Lista de libros sin autenticación:
```bash
# guardamos el token en una variable
ACCESS_TOKEN=$(curl http://localhost:8000/api/token/ -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}' | jq -r '.access')
# imprimimos el token
echo $ACCESS_TOKEN
# imprimimos la lista de libros
curl -X GET http://localhost:8000/api/biblioteca/ -H "Authorization: Bearer $ACCESS_TOKEN"
```

* Lista de libros VIP con autenticación JWT:
```bash
curl -X GET http://localhost:8000/api/sala-vip/ -H "Authorization: Bearer $ACCESS_TOKEN"
```









