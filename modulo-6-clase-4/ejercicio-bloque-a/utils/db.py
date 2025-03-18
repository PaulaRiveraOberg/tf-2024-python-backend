from sqlmodel import Session, SQLModel, create_engine

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URL = "sqlite:///./libreria.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Crear las tablas
SQLModel.metadata.create_all(engine)


# Dependencia para obtener la sesión de la base de datos
def get_session():
    with Session(engine) as session:
        yield session
