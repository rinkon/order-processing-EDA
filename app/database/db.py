from app.core import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:5432/{config.DB_NAME}"
engine= create_engine(db_url)
session=sessionmaker(autoflush=True, autocommit=False,bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()