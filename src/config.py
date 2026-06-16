from pathlib import Path

import os
from dotenv import load_dotenv
# Load the .env variables
load_dotenv()
# Fetch them from the environment
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

# __file__ is the current script. .resolve() gets the full absolute path.
# .parent moves up one folder. 
# Adjust the number of '.parent' calls depending on how deep your script is.
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent  # Assumes script is in a subfolder like /src

# Now construct other paths dynamically
DATA_DIR = PROJECT_ROOT / "data"
SQL_DIR = PROJECT_ROOT / "sql"
ENV_FILE = PROJECT_ROOT / ".env"

# Example: Reading your init.sql safely
sql_file_path = SQL_DIR / "init.sql"
sql_content = sql_file_path.read_text(encoding="utf-8")