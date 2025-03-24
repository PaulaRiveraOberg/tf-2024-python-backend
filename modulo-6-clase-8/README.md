## Clase 7: Tópicos de Seguridad

## CORS

CORS es un mecanismo que permite a las aplicaciones web que se ejecutan en un navegador web accedan a recursos de un servidor que está en una dirección diferente.

Podemos especificar las reglas de CORS en nuestra aplicación fastapi mediante el decorador `add_middleware`.

```python
# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # ⚠️ Solo permitimos acceso desde este origen
    allow_origins=["http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/datos")
def leer_datos():
    return {"mensaje": "¡Hola desde FastAPI con CORS!"}
```

Para probar el ejemplo, podemos crearemos una aplicación frontend con html y js.

```html
<!-- frontend.html -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Frontend externo</title>
</head>
<body>
  <h1>Fetch a FastAPI</h1>
  <button onclick="pedirDatos()">Hacer solicitud</button>
  <pre id="resultado"></pre>

  <script>
    async function pedirDatos() {
      const r = await fetch("http://127.0.0.1:8000/datos", {
        method: "GET",
        credentials: "include" // solo necesario si usas cookies
      });

      const json = await r.json();
      document.getElementById("resultado").textContent = JSON.stringify(json, null, 2);
    }
  </script>
</body>
</html>
```

Utilizaremos el comando `python -m http.server` para servir el frontend y visitar la página `http://localhost:5500/frontend.html`.

```bash
python -m http.server 5500
```

Para ejecutar el servidor fastapi ejecutamos el siguiente comando en otro terminal:

```bash
uvicorn app:app --reload
```

## HTTPS

Generación de certificados mediante `mkcert`:

Instalación:
* OSX:
  * `brew install mkcert`
* Windows:
  * `choco install mkcert`
* Linux:
  * `sudo apt-get install mkcert`

Si no tienes instalado chocolatey en windows, puedes instalarlo previamente con el siguiente comando desde powershell:

```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
# instalar mkcert
choco install mkcert -y
# instalar la CA de mkcert
mkcert -install
```

Generación de certificados:

```bash
mkcert -install
mkcert -key-file key.pem -cert-file cert.pem "localhost"
```

Iniciar servidor fastapi con certificados:

```bash
uvicorn app:app --reload --ssl-keyfile=key.pem --ssl-certfile=cert.pem --host localhost --port 8000
```

Visitar la página `https://localhost:8000/datos` en el navegador.


## Vulnerabilidades de Seguridad en Proyectos Python

Cuando desarrollamos un proyecto python utilizamos múltiples dependencias, estas generalmente las tenemos en un archivo requirements.txt, este archivo se genera con el comando `pip freeze > requirements.txt`.

```bash
pip freeze > requirements.txt
```

Para instalar pip-audit podemos hacerlo mediante pip:

```bash
pip install pip-audit
```

Para ejecutar pip-audit podemos hacerlo con el siguiente comando:

```bash
pip-audit -r requirements.txt
```

Pip audit nos permite actualizar automáticamente las dependencias vulnerables:

```bash
pip-audit -r requirements.txt --fix
```

Safety es otra herramienta que nos permite auditar nuestros proyectos python, esta herramienta contiene una lista de vulnerabilidades de seguridad y nos permite actualizar automáticamente las dependencias vulnerables:

```bash
pip install safety
```

Para ejecutar safety podemos hacerlo con el siguiente comando:

```bash
safety check --full-report
```

Safety check está actualmente deprecado, se recomienda utilizar safety scan, este requiere que nos registramos en la página de safety.


## Ejercicio A: Revisando la seguridad de nuestros proyectos

* Genere el archivo de dependencias de su proyecto requirements.txt
* Instale y ejecute pip-audit en su proyecto para detectar vulnerabilidades en sus dependencias.
* En caso de identificar utiliza fix para intentar corregirlas automáticamente.
* Utilice mkcert para generar un certificado HTTPS y úselo en su servidor de proyecto. 
* En caso de usar django utilice [uvicorn como servidor](https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/uvicorn/) y ejecute el servidor con el certificado mediante el comando `uvicorn myproject.asgi:application --ssl-keyfile=key.pem --ssl-certfile=cert.pem --host localhost --port 8000`.

