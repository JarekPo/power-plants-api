from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

GEONAMES_API_URL = os.getenv("GEONAMES_API_URL")
GEONAMES_USERNAME = os.getenv("GEONAMES_USERNAME")
