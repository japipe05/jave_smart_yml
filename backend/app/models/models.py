from pydantic import BaseModel

class UserRegister(BaseModel):
    email: str
    celular: str
    Nombre: str
    Apellido: str
    tipo_cedula: str
    cedula: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str
