# alembic/env.py

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from db.base import Base  # Your models Base
from db.models import *  # Import models here
# Alembic Config object
config = context.config

# Set up loggers
fileConfig(config.config_file_name)

# Get database URL (same DB, but sync driver!)
db_url = config.get_main_option("sqlalchemy.url")

# 👇 Important: Use SYNC driver here (change mysql+aiomysql to mysql+pymysql)
# e.g., if your original URL is like:
# mysql+aiomysql://user:password@localhost/dbname
# change it to:
# mysql+pymysql://user:password@localhost/dbname

# Setup SQLAlchemy engine with SYNC driver
from sqlalchemy import create_engine

engine = create_engine(
    db_url, poolclass=pool.NullPool
)

# Get your metadata object
target_metadata = Base.metadata

def run_migrations_offline():
    context.configure(
        url=db_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
