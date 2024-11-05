from flask import Flask, render_template
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


if __name__ == '__main__':
    app.run(debug=True)