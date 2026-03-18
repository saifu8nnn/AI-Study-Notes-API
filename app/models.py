from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, func 
from .database import Base

class Note(BaseModel):
    title: str
    content: str

class NoteModel(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())