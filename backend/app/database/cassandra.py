import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

CASSANDRA_USER = os.getenv("CASSANDRA_USER")
CASSANDRA_PASSWORD = os.getenv("CASSANDRA_PASSWORD")
CASSANDRA_PORT = int(os.getenv("CASSANDRA_PORT", 9042))


logger.info(f"Contenido CASSANDRA_USER: {CASSANDRA_USER}")


auth_provider = PlainTextAuthProvider(CASSANDRA_USER, CASSANDRA_PASSWORD)
cluster = Cluster(['localhost'], port=CASSANDRA_PORT, auth_provider=auth_provider)
session = cluster.connect()

# Crear keyspace y tabla
KEYSPACE = "appkeyspace"
session.execute(f"""
    CREATE KEYSPACE IF NOT EXISTS {KEYSPACE}
    WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1'}}
""")
session.set_keyspace(KEYSPACE)

session.execute("""
CREATE TABLE IF NOT EXISTS users (
  email TEXT PRIMARY KEY,
  celular TEXT,
  nombre TEXT,
  apellido TEXT,
  tipo_cedula TEXT,
  cedula TEXT,
  password TEXT
)
""")
