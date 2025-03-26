## Clase 7: Control de Acceso en Django

## Autorización y Permisos

### Configuración inicial

* Primero debemos constar con las dependencias del proyecto, para ello se debe ejecutar el siguiente comando:

```bash
pip install django django-rest-framework djangorestframework_simplejwt
```

* luego crearemos el proyecto y la app:

```bash
django-admin startproject miproyecto
cd miproyecto
django-admin startapp miapp
```

* luego debemos agregar la app a la configuración del proyecto:

```python
# miproyecto/settings.py
INSTALLED_APPS = [
    ...
    'miapp.apps.MiappConfig',
]
```

Crearemos un modelo para gestionar los permisos sobre este, el modelo será `Post` y tendrá los campos `title`, `author`, `body`. este se puede encontrar en el archivo [`models.py`](./miproyecto/miapp/models.py).

Luego correremos las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

Podemos crear un superusuario para poder acceder al admin de django:

```bash
python manage.py createsuperuser
```

### Configuración de permisos

Podemos asignar los permisos sobre nuestro modelo de manera programatica de la siguiente manera:

```python
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from miapp.models import Post

# Crear un usuario
usuario = User.objects.create_user(
    username='normal_user', 
    password='normal_user', 
    is_staff=True, 
    is_superuser=False
)

# Crear un permiso para ver los posts
content_type = ContentType.objects.get_for_model(Post)
permission = Permission.objects.get(
    codename='view_post',
    content_type=content_type
)

# Asignar el permiso al usuario
usuario.user_permissions.add(permission)
```

Podemos crear permisos personalizados para nuestro modelo de la siguiente manera:

```python
# miproyecto/miapp/models.py
class Post(models.Model):
    ...
    class Meta:
        permissions = [('can_publish_post', 'Can publish post'),]
```

Podemos revisar que un usuario tiene permisos sobre un modelo de la siguiente manera:

```python
usuario.has_perm('miapp.can_publish_post')
```

#### Grupos de usuarios

Podemos crear grupos de usuarios y asignar permisos a estos de la siguiente manera:

```python
from django.contrib.auth.models import Group, User, Permission

# Crear un grupo
grupo = Group.objects.create(name='editores')
permiso = Permission.objects.get(codename='change_post')

# Asignar un permiso al grupo
grupo.permissions.add(permiso)
usuario = User.objects.get(username='normal_user')
usuario.groups.add(grupo)
# revisar que el usuario tiene el permiso
usuario.has_perm('miapp.change_post')
```

### RBAC: Role-Based Access Control

Podemos crear roles para nuestros usuarios de la siguiente manera:

```python
# miproyecto/miapp/models.py
from django.db import models

class Post(models.Model):
    ...
    class Meta:
        permissions = [
            ("change_own_post", "Puede editar sus propias publicaciones"),
            ("delete_own_post", "Puede eliminar sus propias publicaciones"),
        ]

class Comment(models.Model):
    ...
    class Meta:
        permissions = [
            ("delete_own_comment", "Puede eliminar sus propios comentarios"),
        ]
```

Luego creamos la migración para los roles:

```bash
python manage.py makemigrations --name crear_roles --app miapp --empty
```

En este archivo se crea una función para crear los roles y otra para eliminarlos.

```python
from django.db import migrations


def crear_roles(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    roles = {
        "Editor": [
            "add_post",
            "change_post",
            "delete_post",
            "view_post",
            "add_comment",
            "delete_comment",
        ],
        "Autor": ["add_post", "change_own_post", "delete_own_post", "view_post"],
        "Lector": ["view_post", "add_comment", "delete_own_comment"],
    }

    for role, permisos in roles.items():
        group, created = Group.objects.get_or_create(name=role)
        for permiso in permisos:
            permission = Permission.objects.get(codename=permiso)
            group.permissions.add(permission)


def eliminar_roles(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name__in=["Editor", "Autor", "Lector"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("miapp", "0003_alter_post_options_comment"),
    ]

    operations = [
        migrations.RunPython(crear_roles, eliminar_roles),
    ]
```

Luego aplicamos la migración:

```bash
python manage.py migrate
```

### Extendiendo el modelo de usuario

Podemos extender el modelo de usuario de varias maneras:

1.- Agregando campos personalizados utilizando `AbstractUser`

```python
# miproyecto/miapp/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    apodo = models.CharField(max_length=255)
    color_favorito = models.CharField(max_length=255)
```

Luego debemos registrar el modelo en el archivo `settings.py`:

```python
# miproyecto/settings.py
AUTH_USER_MODEL = 'miapp.User'
```

2.- Si quieres agregar información adicional, puedes una relación one-to-one con el modelo de usuario.

```python
# miproyecto/miapp/models.py
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apodo = models.CharField(max_length=255)
    color_favorito = models.CharField(max_length=255)
```

Si queremos que el UserProfile se cree automáticamente cuando se crea un usuario, podemos utilizar el signal `post_save`:

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def crear_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
```

Debemos registrar el signal en el archivo `apps.py`:

```python
# miproyecto/miapp/apps.py
from django.apps import AppConfig

class MiappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'miapp'

    def ready(self):
        import miapp.signals
```

### Decoradores de autenticación

Podemos utilizar los decoradores de autenticación de django para proteger nuestras vistas. Podemos usar los siguientes decoradores:

* `@login_required`: para proteger una vista para que solo los usuarios autenticados puedan acceder a ella.
* `@login_not_required`: para proteger una vista para que solo los usuarios no autenticados puedan acceder a ella.
* `@permission_required`: para proteger una vista para que solo los usuarios con un permiso específico puedan acceder a ella.

```python
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def profile_view(request):
    return render(request, 'miapp/profile.html')

@login_required
@permission_required("miapp.add_post", raise_exception=True)
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")
        Post.objects.create(title=title, body=body, author=request.user)
        return redirect("miapp:profile")
    else:
        return render(request, "miapp/create_post.html")
```

### Decoradores y mixins de autenticación en DRF

Podemos utilizar los decoradores y mixins de autenticación en DRF para proteger nuestras vistas. Podemos usar los siguientes decoradores:

* `@api_view`: nos permite crear vistas que responden a peticiones HTTP a métodos específicos.
* `@authentication_classes`: nos permite especificar el sistema de autenticación que se utilizará para la vista.
* `@permission_classes`: nos permite especificar los permisos que se utilizarán para la vista.

También Podemos usar mixin para vistas basadas en clases, en este caso también  podemos conectar DRF con el sistema de permisos de Django, utilizando el decorador @permission_classes con DjangoModelPermissions. Al usar este de acuerdo al metodo se solicitará un permiso adecuado:
* `POST`: permiso `add` del modelo
* `PUT` y `PATCH`: permiso `change` del modelo
* `DELETE`: permiso `delete` del modelo


```python
from miapp.models import Post
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [DjangoModelPermissions]
```

Podemos también especificar permisos personalizados para una vista en particular, para esto debemos crear un permiso personalizado y asignarle el permiso a la vista.

```python
from rest_framework.permissions import BasePermission

class CanEditOwnPostPermission(BasePermission):
    """
    Permiso personalizado para verificar si el usuario tiene el permiso 'change_own_post' en un modelo.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return request.user.has_perm("miapp.change_own_post")
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
```

Podemos utilizar este permiso en una vista en particular:

```python
class MyPostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [CanEditOwnPostPermission]

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)
```

finalmente debemos registrar la vista en el router:

```python
from django.urls import include, path
from rest_framework import routers

from .views import MyPostViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"my-posts", MyPostViewSet, basename="my-posts")

urlpatterns = [
    path("", include(router.urls)),
]
```
