from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)


# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')


# Ruta para la página "Acerca de"
@app.route('/about')
def about():
    group = {
        'name': "Grupo de Desarrollo Web",
        'description': "Nuestro objetivo es aprender los fundamentos de desarrollo backend con Flask.",
        'members': ["Ana", "José", "Luis", "Carla"],
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    return render_template('about.html', group=group)


# Ruta para la página de perfil con query string
@app.route('/perfil')
def perfil():
    # Obtener los parámetros de query string con valores predeterminados
    nombre = request.args.get('nombre', 'Invitado')
    edad = request.args.get('edad', 'Desconocida')
    profesion = request.args.get('profesion', 'Estudiante')

    return render_template(
        'perfil.html',
        nombre=nombre,
        edad=edad,
        profesion=profesion
    )

anuncios_list = []

# Ruta para publicar un anuncio
@app.route('/anuncio', methods=['GET', 'POST'])
def anuncio():
    if request.method == 'POST':
        # Obtener datos del formulario
        titulo = request.form.get('titulo')
        contenido = request.form.get('contenido')
        prioridad = request.form.get('prioridad', 'media')

        # Validar que los campos obligatorios tengan datos
        if titulo and contenido:
            # Crear un diccionario para el anuncio
            nuevo_anuncio = {
                'titulo': titulo,
                'contenido': contenido,
                'prioridad': prioridad,
                'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            # Guardar el anuncio en la lista
            anuncios_list.append(nuevo_anuncio)
            return redirect(url_for('anuncios'))  # Redirigir a la página de anuncios
        else:
            # Mensaje de error si faltan datos obligatorios
            error = "El título y contenido son obligatorios."
            return render_template('anuncio.html', error=error)

    # Método GET: Mostrar formulario
    return render_template('anuncio.html')


# Ruta para mostrar todos los anuncios
@app.route('/anuncios')
def anuncios():
    return render_template('anuncios.html', anuncios=anuncios_list)

if __name__ == '__main__':
    app.run(debug=True)