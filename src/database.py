from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *


engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True
)


session_factory = sessionmaker(engine)

def create_tables():
    Model.metadata.create_all(bind=engine)

def drop_tables():
    Model.metadata.create_all(bind=engine)