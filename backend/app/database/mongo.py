from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from urllib.parse import quote_plus
from dotenv import load_dotenv
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

env_path = Path(__file__).resolve().parents[2] / '.env'
load_dotenv(dotenv_path=env_path)

# Log para verificar si las variables de entorno se cargan correctamente
logger.info(f"{env_path}")

#MONGO_HOST = os.getenv("MONGO_HOST","localhost")
MONGO_HOST = os.getenv("MONGO_HOST","mongo")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_DB = os.getenv("MONGO_DB","db_zip_analysis_jave")
MONGO_USUARIO = os.getenv("MONGO_USUARIO","felipe")
MONGO_CREDENCIAL = os.getenv("MONGO_CREDENCIAL","2135654felipedsaf54654aAndressdf545")


MONGO_URI = f"mongodb://{MONGO_USUARIO}:{MONGO_CREDENCIAL}@{MONGO_HOST}:{MONGO_PORT}"

logger.info(f"Contenido MONGO_URI: {MONGO_URI}")
#MONGO_URI = f"mongodb://felipe:2135654felipedsaf54654aAndressdf545@localhost:27017"

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]




