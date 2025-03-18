from pydantic import BaseModel, EmailStr


class Usuario(BaseModel):
    username: str
    email: str
    hashed_password: str
    is_active: bool = True

    def to_mongo(self):
        return {
            "username": self.username,
            "email": self.email,
            "hashed_password": self.hashed_password,
            "is_active": self.is_active,
        }

    @classmethod
    def from_mongo(cls, data):
        return cls(**data)


class UsuarioCreate(BaseModel):
    username: str
    email: str
    password: str


class UsuarioResponse(BaseModel):
    username: str
    email: str
    is_active: bool
