from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, func ,Text
from .database import Base
from typing import Optional
from pydantic import Field

class Note(BaseModel):
    title: str
    content: str = Field(min_length=1)
    summary:Optional[str]=None

class NoteModel(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    summary = Column(Text,nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())