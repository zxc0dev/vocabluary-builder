import psycopg

from logger import init_logging
init_logging()

from loguru import logger





# Create a connection to the database
logger.info('Connecting to the database...')

conn = psycopg.connect(f"dbname={db_name} user={db_user} password={db_password}")


logger.info('Connection is successful.')


