from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class About(Base):
    __tablename__ = "about"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    headline = Column(String, nullable=False)
    bio = Column(Text, nullable=False)
    location = Column(String, nullable=True)
    email = Column(String, nullable=True)
    github = Column(String, nullable=True)
    linkedin = Column(String, nullable=True)
    profile_image = Column(String, nullable=True)
