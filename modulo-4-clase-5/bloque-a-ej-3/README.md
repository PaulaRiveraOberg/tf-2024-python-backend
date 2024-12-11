## Bloque A Ejercicio 2

Para correr el servidor, usamos el siguiente comando:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000 --reload
```

Para probar el endpoint podemos utilizar curl con las siguientes peticiones :

```bash
curl -X POST "http://localhost:8000/libro/buscar" -H "Content-Type: application/json" -d '{"fecha_inicial": "1960-01-01", "fecha_final": "1970-01-01"}'
```

Esta solicitud devuelve el primer libro que se encuentre entre las fechas indicadas:

```json
{
  "titulo": "Cien años de soledad",
  "autor": "García Márquez",
  "fecha": "1967-05-30"
}
```
