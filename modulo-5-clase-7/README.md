## Clase 7: Pruebas de Performance con Apache JMeter

Se incluye un proyecto de Django para poder realizar las pruebas de performance en el directorio `myproject`.


## Pruebas de Performance Django

Puede probar los distintos escenarios de como ejecutar su servidor:

```bash
python manage.py runserver
```

Desactivando threads:

```bash
python manage.py runserver --nothreading
```

Corriendo con uvicorn:

```bash
# instalar uvicorn
pip install uvicorn

# correr con uvicorn
uvicorn myproject.asgi:application --workers 4
```

## Ejercicio A: Testeando el Performance de Acceso a los Datos

1. Diseñe una API sencilla que permita responder alguna consulta de datos como las que ya hemos estado trabajando.
2. Ahora usted puede elegir entre implementar la API con Django o con FastAPI.
3. NO use autenticación. Queremos concentrarnos en las pruebas y no en la configuración de la autenticación.
4. Diseñe 5 pruebas distintas y ejecute.
5. Recuerde revisar los resultados y verificar que las conexiones se están realizando.

