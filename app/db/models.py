# app/db/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

# Document model/table
class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    doc_type = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)