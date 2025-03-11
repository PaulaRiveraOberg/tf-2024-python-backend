## Clase 2: Token Auth y JWT

## Token Auth en Django

### Configuración inicial

* Primero debemos constar con las dependencias del proyecto, para ello se debe ejecutar el siguiente comando (con esto instalaremos tambien `djangorestframework-simplejwt` que utilizaremos en la sección de JWT):

```bash
pip install django django-rest-framework djangorestframework-simplejwt
```

* luego crearemos el proyecto y la app:

```bash
django-admin startproject miapi
cd miapi
django-admin startapp autenticacion
```

* también debemos agregar la app y la configuración en el archivo `settings.py`:

```python
# settings.py
... # otras configuracion
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'autenticacion.apps.AutenticacionConfig',
]
...
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
```

* Luego corremos las migraciones:

```bash
python manage.py migrate
```

esto permitirá autenticarnos mediante `TokenAuthentication` usuando los usuarios creados en la autenticación de Django, `django-contrib-auth`.

* Para habilitar la creación automática de tokens para los usuarios podemos usar signals y crear un token para el usuario cuando se crea:

```python
# autenticacion/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

debemos agregar el signal al archivo `apps.py`:

```python
# autenticacion/apps.py
from django.apps import AppConfig

class AutenticacionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'autenticacion'
    def ready(self):
        import autenticacion.signals
```

* Luego debemos agregar el token a la respuesta de la API:

```python
# autenticacion/serializers.py
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TokenSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = ['key', 'user']
```

* Para crear un endpoint para obtener el token de un usuario, debemos agregar el siguiente código en el archivo `urls.py`:

```python
# miapi/urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
```

Podemos encontrar el proyecto completo en [miapi](./miapi/)

## JWT

Mediante JWT podemos generar tokens para nuestros usuarios, estos tokens pueden ser usados para autenticar a los usuarios en nuestras APIs. Para agregar JWT a nuestro proyecto, debemos seguir los siguientes pasos:

* Si no lo instalamos previamente debemos ejecutar el siguiente comando para instalar `djangorestframework-simplejwt`:

```bash
pip install djangorestframework-simplejwt
```

* Luego debemos agregar las configuraciones en el archivo `settings.py`:

```python
# miapi/settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    'autenticacion.apps.AutenticacionConfig',
]
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
```

* Luego debemos agregar los endpoints para obtener el token y refrescarlo en el archivo `urls.py`:

```python
# miapi/urls.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
```

Podemos encontrar el proyecto completo en [miapi](./miapi/)

## Custom JWT Claims

Podemos agregar claims personalizados a nuestro token JWT, para ello debemos seguir los siguientes pasos:

* Para agregar claims a nuestro JWT, debemos agregar el siguiente código en el archivo `settings.py`:

```python
# miapi/settings.py
SIMPLE_JWT = {
    "TOKEN_OBTAIN_SERIALIZER": "autenticacion.serializers.MyTokenObtainPairSerializer",
}
```

* Luego debemos agregar el siguiente código en el archivo `serializers.py` de la app `autenticacion`:

```python
# autenticacion/serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        return token
```

Podemos encontrar el proyecto completo en [miapi](./miapi/)


## Ejercicio A: Implementando JWT en DRF

* Utilizando el proyecto de administración de libros en DRF de la clase anterior, desactive la autenticación mediante Basic Http Auth y habilite mediante JWT
    * Cree los endpoints para solicitar un token, renovar y verificar
* Cree los Request de prueba en Postman para probar los endpoints anteriores: 
* Ingrese a https://jwt.io/#debugger y revise el contenido del token generado

* Solución: [ejercicio-bloque-b](./ejercicio-bloque-b/README.md) (se encuentra en conjunto con la solución del bloque B)

## Ejercicio B: Personalización de Token JWT en DRF
* Modifique el serializador de obtención de token para agregar:
    * si el usuario es admin
    * Su email y nombre
* Verifique mediante https://jwt.io/#debugger que se incluyan las nuevas variables.
* Compruebe decodificando mediante base64 los primero 2 componentes del token que genero, utilizando una herramienta como https://www.base64decode.org/ 
* Discuta con su grupo porque no puedo modificar los claims o header de un token, que ocurriría?

* Solución: [ejercicio-bloque-b](./ejercicio-bloque-b/README.md)
