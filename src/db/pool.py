from psycopg_pool import ConnectionPool
from loguru import logger
from src.config import db_name, db_user, db_password

logger.debug("Creating a connection pool...")

pool = ConnectionPool(
    conninfo=f"dbname={db_name} user={db_user} password={db_password} host=localhost",
    min_size=1,
    max_size=10,
    open=True,
)

logger.debug("The connection pool has been created.")