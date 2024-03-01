from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(".") / ".env"

DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
