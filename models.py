from sqlalchemy import Column, Integer, String
from app.database import Base

class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False)

# Add this for logging table
from sqlalchemy import DateTime
from datetime import datetime

class APILog(Base):
    __tablename__ = "api_logs"

    id = Column(Integer, primary_key=True, index=True)
    method = Column(String)
    url = Column(String)
    status_code = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
