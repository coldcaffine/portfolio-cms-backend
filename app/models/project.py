from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    tech_stack = Column(String, nullable=True)
    github_url = Column(String, nullable=True)
    live_url = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
