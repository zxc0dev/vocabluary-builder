INSERT INTO words (word_lang, word_sk, word_en, word_ru)
VALUES (%(word_lang)s, %(word_sk)s, %(word_en)s, %(word_ru)s)
RETURNING id;