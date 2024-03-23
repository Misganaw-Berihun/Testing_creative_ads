import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv(override=True)

def create_database_engine():
    DATABASE_URL = os.environ.get('DATABASE_URL')
    return create_engine(DATABASE_URL)