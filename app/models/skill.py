from sqlalchemy import Column, Integer, String
from app.database import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    level = Column(String, nullable=True)
