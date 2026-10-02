from typing import Optional
from pydantic import BaseModel, EmailStr


class AboutBase(BaseModel):
    name: str
    headline: str
    bio: str
    location: Optional[str] = None
    email: Optional[EmailStr] = None
    github: Optional[str] = None
    linkedin: Optional[str] = None
    profile_image: Optional[str] = None


class AboutCreate(AboutBase):
    pass


class AboutUpdate(BaseModel):
    name: Optional[str] = None
    headline: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    email: Optional[EmailStr] = None
    github: Optional[str] = None
    linkedin: Optional[str] = None
    profile_image: Optional[str] = None


class AboutResponse(AboutBase):
    id: int

    class Config:
        from_attributes = True
