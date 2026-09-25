from sqlalchemy import Column, Integer, String
from app.database import Base


class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    file_url = Column(String, nullable=False)
    file_type = Column(String, nullable=True)
