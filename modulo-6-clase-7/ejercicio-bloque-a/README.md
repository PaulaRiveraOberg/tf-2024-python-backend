# Ejercicio A

Para instalar las dependencias, ejecutar:

```bash
pip install django 
```

Luego se deben correr las migraciones:

```bash
python manage.py migrate
```

Implementamos la creación del nuevo rol `Moderador` y los permisos asociados a traves de la migración `miapp/migrations/0003_auto_20250320_1813.py`.

Podemos crear un usuario con el rol `Moderador` desde el shell de django, mediante el siguiente codigo:

```python
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

user = User.objects.create_user(username='moderador', password='moderador', is_staff=True)
group = Group.objects.get(name='Moderador')
user.groups.add(group)
```

Luego podemos correr el servidor:

```bash
python manage.py runserver
```

Si visitamos el admin en `http://localhost:8000/admin/` y entramos con el usuario `moderador` y password `moderador`, podemos ver que el usuario tiene el rol `Moderador` y los permisos asociados.

Los permisos que tiene el usuario `moderador` son:
- `add_post`
- `change_own_post`
- `delete_own_post`
- `view_post`
- `add_comment`
- `delete_comment`

Por lo tanto podemos agregar y ver post pero no los comentarios.


