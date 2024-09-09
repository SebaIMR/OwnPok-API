from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
from google.cloud.sql.connector import Connector

# Configurar el conector de Google Cloud SQL
connector = Connector()

def getconn():
    """
    Establece una conexión a la base de datos usando el conector de Google Cloud SQL.
    """
    try:
        conn = connector.connect(
            settings.instance_connection_name,
            "pg8000",
            user=settings.db_user,
            password=settings.db_pass,
            db=settings.db_name
        )
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise

# Configurar el motor de SQLAlchemy con la función de conexión personalizada
engine = create_engine(
    "postgresql+pg8000://",  # Driver para PostgreSQL utilizando pg8000
    creator=getconn,         # Función personalizada para crear la conexión
)

# Crear una fábrica de sesiones que se enlaza con el motor
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para definir modelos de la base de datos
Base = declarative_base()

def get_db():
    """
    Proporciona una sesión de base de datos y garantiza que se cierre correctamente.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()