from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from app.database import get_db
from app.models.message import Message
from app.schemas.message import MessageCreate
from app.config import settings


router = APIRouter(
    prefix="/contact",
    tags=["Contact"]
)


mail_config = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
)


@router.post("/")
def create_message(
    message: MessageCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    new_message = Message(
        name=message.name,
        email=message.email,
        subject=message.subject,
        message=message.message
    )

    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    email_message = MessageSchema(
        subject=message.subject or "New Portfolio Contact",
        recipients=[settings.MAIL_USERNAME],
        body=f"""
New message from your portfolio:

Name: {message.name}
Email: {message.email}
Subject: {message.subject or "No subject"}

Message:
{message.message}
""",
        subtype="plain"
    )

    fast_mail = FastMail(mail_config)

    background_tasks.add_task(
        fast_mail.send_message,
        email_message
    )

    return {
        "message": "Message sent successfully",
        "id": new_message.id
    }
