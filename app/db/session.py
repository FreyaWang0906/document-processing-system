# app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# PostgreSQL connection URL
DATABASE_URL = "postgresql://admin:admin@docdb:5432/docsys"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)