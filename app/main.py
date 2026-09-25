from fastapi import FastAPI

from app.database import Base, engine
from app.routers import (
    auth,
    about,
    skills,
    projects,
    blogs,
    experience,
    testimonials,
    services,
    upload,
    contact,
)
from app.models import user
from app.models import about as about_model
from app.models import skill as skill_model
from app.models import experience as experience_model
from app.models import testimonial as testimonial_model
from app.models import service as service_model
from app.models import media as media_model
from fastapi.staticfiles import StaticFiles
from app.models import message as message_model
Base.metadata.create_all(bind=engine)


app = FastAPI(title="Portfolio CMS API")

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.include_router(auth.router)
app.include_router(about.router)
app.include_router(skills.router)
app.include_router(projects.router)
app.include_router(blogs.router)
app.include_router(experience.router)
app.include_router(testimonials.router)
app.include_router(services.router)
app.include_router(upload.router)
app.include_router(contact.router)


@app.get("/")
def root():
    return {"status": "ok"}
