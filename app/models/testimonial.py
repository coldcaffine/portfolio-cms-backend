from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Testimonial(Base):
    __tablename__ = "testimonials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=True)
    content = Column(Text, nullable=False)
    image_url = Column(String, nullable=True)
