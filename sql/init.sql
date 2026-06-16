DROP TABLE IF EXISTS vocab

CREATE TABLE vocab (
    id INT PRIMARY KEY,
    word_lang VARCHAR(2) NOT NULL,
    word_sk VARCHAR(64) NOT NULL,
    word_en VARCHAR(64) NOT NULL,
    word_ru VARCHAR(64) NOT NULL,
    added_at DATE DEFAULT CURRENT_DATE,
    next_review_date DATE DEFAULT (CURRENT_DATE + INTERVAL '3 days'),
    current_interval_days INT DEFAULT 3
);