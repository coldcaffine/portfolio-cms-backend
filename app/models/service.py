from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    icon = Column(String, nullable=True)
