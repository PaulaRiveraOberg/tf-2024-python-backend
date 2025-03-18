from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models.users import Usuario
from passlib.context import CryptContext
from pymongo import MongoClient
from utils.database import get_database

# Configuración de seguridad
security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

user = {
    "username": "roberto",
    "hashed_password": "$2a$12$YWZQ6csAPJ1sX7fcHtRJ8.DW/iHP4XO.BGylHaa6/uNtz8WSVNuaa",
}


# Funciones de autenticación
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def get_current_user(
    credentials: HTTPBasicCredentials = Depends(security),
    # db: MongoClient = Depends(get_database),
) -> Usuario:
    # user = db.usuarios.find_one({"username": credentials.username})
    if not user or not verify_password(credentials.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user
