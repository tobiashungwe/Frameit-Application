import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Read MySQL credentials from environment variables, or set defaults
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# 2. Build the database URL for mysql+pymysql
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 3. Create the SQLAlchemy engine
#    - echo=True shows SQL logs in console, good for debugging.
#    - future=True enforces the 2.0 style usage.
engine = create_engine(DATABASE_URL, echo=False, future=True)

# 4. Create a configured "SessionLocal" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Create a base class for your models to inherit
Base = declarative_base()


def get_db_session():
    """
    Dependency that will be used in FastAPI endpoints.
    Yields a database session, then closes it after the request finishes.

    Example usage in a FastAPI route:

        from fastapi import Depends
        from .database import get_db_session

        @app.get("/items/")
        def read_items(db: Session = Depends(get_db_session)):
            return db.query(Item).all()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
