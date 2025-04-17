from fastapi import APIRouter, Form, UploadFile, File, HTTPException, FastAPI
from app.models.models import UserRegister, UserLogin
from app.database.cassandra import session
import bcrypt
import logging
from jose import JWTError, jwt
from datetime import datetime, timedelta

from fastapi.responses import JSONResponse


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["Auth"])

#login y registro

@router.post("/register", tags=["Auth"])
def register(user: UserRegister):
    existing_user = session.execute(
        "SELECT * FROM users WHERE email=%s", (user.email,)
    ).one()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # Hashear la contraseña
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    session.execute("""
        INSERT INTO users (email, celular, Nombre, Apellido, tipo_cedula, cedula, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        user.email, user.celular, user.Nombre,
        user.Apellido, user.tipo_cedula,
        user.cedula, hashed_password.decode('utf-8')  # Guardamos como string
    ))

    return {"message": "User registered successfully"}


@router.post("/login", tags=["Auth"])
def login(user: UserLogin):
    # Buscar por email o celular
    result = session.execute(
        "SELECT * FROM users WHERE email=%s ALLOW FILTERING", 
        (user.email,)
    ).one()

    if not result:
        result = session.execute(
            "SELECT * FROM users WHERE celular=%s ALLOW FILTERING", 
            (user.email,)
        ).one()

    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not bcrypt.checkpw(user.password.encode('utf-8'), result.password.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Crear token
    token_data = {
        "sub": str(result.email),  # Puedes poner aquí user_id, email, etc.
        "nombre": result.nombre,
    }
    access_token = create_access_token(token_data)

    # Devolver token y mensaje
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "message": f"Bienvenido {result.nombre}",
    }

# Configuración
SECRET_KEY = "tu_clave_secreta_segura"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 hora

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
