from pymongo import MongoClient
from pymongo.database import Database

# Configuración de la conexión a MongoDB
MONGO_URL = "mongodb://localhost:27017/"
DATABASE_NAME = "libreria"


def get_database() -> Database:
    client = MongoClient(MONGO_URL)
    return client[DATABASE_NAME]


# Crear índices necesarios
def setup_indexes():
    db = get_database()

    # Índices para la colección de usuarios
    db.usuarios.create_index("username", unique=True)
    db.usuarios.create_index("email", unique=True)

    # Índices para la colección de libros
    db.libros.create_index("isbn", unique=True)

    # Índices para la colección de reviews
    db.reviews.create_index([("isbn", 1), ("usuario", 1)], unique=True)
