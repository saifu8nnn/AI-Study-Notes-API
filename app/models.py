from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, func 
from .database import Base
from typing import Optional

class Note(BaseModel):
    title: str
    content: str
    summary:Optional[str]=None

class NoteModel(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(String, nullable=False)
    summary = Column(String,nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())