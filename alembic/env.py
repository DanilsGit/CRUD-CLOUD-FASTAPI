from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
import os
import sys
from dotenv import load_dotenv

# ---- Configura paths ----
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)

# ---- Carga variables de entorno ----
load_dotenv()

# ---- Configuración de Alembic ----
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ---- Importa la Base y modelos ----
from db.database import Base  # Ajusta según tu estructura
from models.event import Event  # Importa modelos para autogenerate
target_metadata = Base.metadata

def get_db_url():
    url = os.getenv("DB_URL") or config.get_main_option("sqlalchemy.url")
    print(f"Using DB URL: {url}")  # Debug
    return url

def run_migrations_online():
    """Ejecuta migraciones en modo online (conexión real a la BD)"""
    engine = create_engine(
        get_db_url(),
        poolclass=pool.NullPool,
    )

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )
        with context.begin_transaction():
            context.run_migrations()

# ---- Ejecuta según el modo ----
if context.is_offline_mode():
    context.configure(
        url=get_db_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()
else:
    run_migrations_online()