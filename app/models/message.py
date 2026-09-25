from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    subject = Column(String, nullable=True)
    message = Column(Text, nullable=False)
