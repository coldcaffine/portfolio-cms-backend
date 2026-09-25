from pydantic import BaseModel, EmailStr


class MessageCreate(BaseModel):
    name: str
    email: EmailStr
    subject: str | None = None
    message: str
