from sqlalchemy import Column, Integer, String, DateTime
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from db.database import Base

# SQLAlchemy model
class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    location = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

# Pydantic models (schemas)
class EventBase(BaseModel):
    title: str
    description: str
    location: str
    start_time: datetime
    end_time: datetime

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

class EventResponse(EventBase):
    id: int
    
    class Config:
        orm_mode = True
        from_attributes = True