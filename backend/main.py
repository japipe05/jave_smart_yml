import openai
import os
from dotenv import load_dotenv
# main.py o donde inicialices tu app
from app.models.prompt_model import Base
from app.database.postgres import engine

from http import client
from fastapi import FastAPI, UploadFile, File, Form, Depends
from pathlib import Path
import shutil
from fastapi.middleware.cors import CORSMiddleware
import logging

from public.insert_prompt import ensure_prompt_exists

# Configurar logging
log_file = Path("logs/server.log")
log_file.parent.mkdir(parents=True, exist_ok=True)  # Crea la carpeta si no existe
#Creamos el modelo
Base.metadata.create_all(bind=engine)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
) 

logger = logging.getLogger(__name__)  # Se debe crear aquí para asegurar que todo lo registre bien

# Configuración de la aplicación utilizando el Factory Pattern
def create_app():
    app = FastAPI(title="FastAPI File Upload", version="1.0")
    
    # Importar y registrar rutas
    from app.routes import file_routes, auth_routers
    app.include_router(file_routes.router)
    app.include_router(auth_routers.router)
    
    return app

app = create_app()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
models = client.models.list()
#for model in models.data:
#    print(model.id)

# Llamar al inicio de la app
ensure_prompt_exists()
frontend_url = os.getenv("FRONTEND_URL")
# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url],  # Permite solicitudes desde el frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)





