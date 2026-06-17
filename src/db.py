# PostgreSQL driver
import psycopg

# Logging
from loguru import logger

# Config
from src.config import db_name, db_user, db_password, SQL_DIR

def _read_query(file_name, subdir='', encoding='utf-8'):
    if subdir != '':
        full_path = SQL_DIR / subdir / file_name
    else:
        full_path = SQL_DIR / file_name
    try:
        return full_path.read_text(encoding=encoding)
    except FileNotFoundError:
        logger.info(f"SQL file not found: {full_path}")
        raise

# Create a connection to the database
def _connect():
    logger.info('Connecting to the database...')

    conn = psycopg.connect(f"dbname={db_name} user={db_user} password={db_password}")

    logger.info('Connection is successful.')
    return conn

ADD_WORD = _read_query('add_word.sql')

# Add a word into the table
def add_word(word_lang, word_sk, word_en, word_ru):
    with _connect() as conn:
        with conn.cursor() as cur:
            cur.execute(ADD_WORD, {
                "word_lang": word_lang,
                "word_sk": word_sk,
                "word_en": word_en,
                "word_ru": word_ru
            })
            row = cur.fetchone()
            if row is not None:
                word_id = row[0]
                logger.info(f"Successfully inserted word with ID: {word_id}")
                return word_id
            else:
                logger.error("Query executed, but no ID was returned.")
                return None
    