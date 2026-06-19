INSERT INTO sentences (word_id, sentence_lang, sentence)
VALUES (%(word_id)s, %(sentence_lang)s, %(sentence)s)
RETURNING id;