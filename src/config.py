from pathlib import Path

import os
from dotenv import load_dotenv

# Load the .env variables
load_dotenv()

# Fetch them from the environment
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")

# Current directory
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent

# Construct other paths
SQL_DIR = PROJECT_ROOT / "sql"
SQL_WORDS_REPO = PROJECT_ROOT / "sql/words_repo"
ENV_FILE = PROJECT_ROOT / ".env"

# Claude prompts
ANSWER_PROMPT = ""
QUESTION_PROMPT = ""
