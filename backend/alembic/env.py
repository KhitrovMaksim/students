import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from models import Base

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

db_name = config.config_ini_section

TEST_SERVER_DB_PASSWORD = os.environ.get('TEST_SERVER_DB_PASSWORD')
TEST_SERVER_HOST = os.environ.get('TEST_SERVER_HOST')

config.set_main_option(
    "sqlalchemy.url",
    f"mysql+pymysql://teacher:{TEST_SERVER_DB_PASSWORD}@{TEST_SERVER_HOST}:3306/students"
)


def run_migrations_offline():

    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
