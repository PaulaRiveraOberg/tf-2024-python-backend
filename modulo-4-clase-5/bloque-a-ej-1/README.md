## Bloque A Ejercicio 1

Para correr el servidor, usamos el siguiente comando:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000 --reload
```

Para probar el endpoint podemos visitar las siguiente URLs:


* http://localhost:8000/libro/El%20Quijote/Cervantes/1605
* http://localhost:8000/libro/Ana%20Karenina/Tolstoi/1877
