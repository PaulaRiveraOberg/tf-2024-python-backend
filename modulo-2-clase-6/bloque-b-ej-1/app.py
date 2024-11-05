from crypt import methods

from flask import Flask, render_template, request
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


if __name__ == '__main__':
    app.run(debug=True)