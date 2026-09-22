from fastapi import FastAPI

from app.database import Base, engine
from app.routers import auth, about
from app.models import user
from app.models import about as about_model


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Portfolio CMS API")

app.include_router(auth.router)
app.include_router(about.router)


@app.get("/")
def root():
    return {"status": "ok"}
