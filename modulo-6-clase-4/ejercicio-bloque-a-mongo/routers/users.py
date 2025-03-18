from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from models.users import Usuario, UsuarioCreate, UsuarioResponse
from passlib.context import CryptContext
from pymongo import MongoClient
from utils.database import get_database

router = APIRouter(prefix="/usuarios", tags=["usuarios"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UsuarioCreate, db: MongoClient = Depends(get_database)):
    # Verificar si el usuario ya existe
    if db.usuarios.find_one({"username": user.username}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre de usuario ya está en uso",
        )

    if db.usuarios.find_one({"email": user.email}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El email ya está en uso"
        )

    # Crear el usuario
    hashed_password = pwd_context.hash(user.password)
    new_user = Usuario(
        username=user.username, email=user.email, hashed_password=hashed_password
    )

    db.usuarios.insert_one(new_user.to_mongo())
    return new_user


@router.get("/", response_model=List[UsuarioResponse])
async def get_users():
    db = get_database()
    user_data = db.usuarios.find()

    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado"
        )

    return [Usuario.from_mongo(user) for user in user_data]
