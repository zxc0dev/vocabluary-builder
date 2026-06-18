from loguru import logger
from src.config import SQL_WORDS_REPO


class WordsRepository:
    def __init__(self, pool):
        self.pool = pool
        self.add_word_sql = (SQL_WORDS_REPO / "add_word.sql").read_text()
        self.fetch_words_sql = (SQL_WORDS_REPO / "fetch_words.sql").read_text()

    def add_word(self, word_lang, word_sk, word_en, word_ru, word_ua):
        try:
            logger.debug('Inserting word...')
            with self.pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        self.add_word_sql,
                        {
                            "word_lang": word_lang,
                            "word_sk": word_sk,
                            "word_en": word_en,
                            "word_ru": word_ru,
                            "word_ua": word_ua,
                        },
                    )
                    row = cur.fetchone()
                    if row is None:
                        logger.error("Query executed, but no ID was returned.")
                        return None
                    logger.debug(f"Inserted word with ID: {row[0]}")
                    return row[0]
        except Exception as e:
            logger.exception(f'Failed to insert word {e}.')
            raise

    def fetch_words(self):
        try:
            logger.debug("Fetching words...")
            with self.pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(self.fetch_words_sql)
                    return cur.fetchall()
        except Exception as e:
            logger.exception(f'Failed to fetch words {e}.')
            raise