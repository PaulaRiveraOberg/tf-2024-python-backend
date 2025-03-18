from sqlmodel import Field, SQLModel


class Usuario(SQLModel, table=True):
    username: str = Field(primary_key=True)
    email: str = Field(unique=True)
    hashed_password: str
    is_active: bool = Field(default=True)


class UsuarioCreate(SQLModel):
    username: str
    email: str
    password: str


class UsuarioResponse(SQLModel):
    username: str
    email: str
    # hashed_password: str
    is_active: bool
