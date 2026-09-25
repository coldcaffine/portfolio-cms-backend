from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Experience(Base):
    __tablename__ = "experience"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, nullable=False)
    company = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    start_date = Column(String, nullable=True)
    end_date = Column(String, nullable=True)
