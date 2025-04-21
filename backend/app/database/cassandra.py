import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.policies import DCAwareRoundRobinPolicy  # Import the load balancing policy
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

CASSANDRA_USER = os.getenv("CASSANDRA_USER", "cassandra_admin")
CASSANDRA_PASSWORD = os.getenv("CASSANDRA_PASSWORD", "supersecure")
CASSANDRA_PORT = int(os.getenv("CASSANDRA_PORT", 9042))
CASSANDRA_PROTOCOL_VERSION = int(os.getenv("CASSANDRA_PROTOCOL_VERSION", 4))  # Adjust the protocol version if necessary

logger.info(f"Contenido CASSANDRA_USER: {CASSANDRA_USER}")

auth_provider = PlainTextAuthProvider(CASSANDRA_USER, CASSANDRA_PASSWORD)

# Add the load balancing policy explicitly
load_balancing_policy = DCAwareRoundRobinPolicy(local_dc='dc1')  # Replace 'dc1' with your actual data center name

# Now include the load balancing policy and protocol version in the Cluster constructor
cluster = Cluster(
    #['localhost'],
    ['cassandra'],
    port=CASSANDRA_PORT,
    #auth_provider=auth_provider,
    load_balancing_policy=load_balancing_policy,
    protocol_version=CASSANDRA_PROTOCOL_VERSION  # Specify the protocol version explicitly
)

session = cluster.connect()

# Create keyspace and table
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
