from typing import List

from fastapi import APIRouter, Depends, HTTPException
from models.users import Usuario, UsuarioCreate, UsuarioResponse
from sqlmodel import Session, select
from utils.auth import get_password_hash
from utils.db import get_session

router = APIRouter()


# Rutas para usuarios
@router.post("/usuarios/", response_model=UsuarioResponse)
async def crear_usuario(
    usuario: UsuarioCreate, session: Session = Depends(get_session)
):
    # Verificar si el username ya existe
    if session.get(Usuario, usuario.username):
        raise HTTPException(status_code=400, detail="El username ya existe")

    # Verificar si el email ya existe
    existing_email = session.exec(
        select(Usuario).where(Usuario.email == usuario.email)
    ).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="El email ya existe")

    # Crear el usuario con la contraseña hasheada
    db_usuario = Usuario(
        username=usuario.username,
        email=usuario.email,
        hashed_password=get_password_hash(usuario.password),
        is_active=True,
    )

    session.add(db_usuario)
    session.commit()
    session.refresh(db_usuario)
    return db_usuario


@router.get("/usuarios/", response_model=List[UsuarioResponse])
async def listar_usuarios(session: Session = Depends(get_session)):
    usuarios = session.exec(select(Usuario)).all()
    return usuarios
