from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine

app = FastAPI(title="Portfolio CMS API")


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return {"database": "connected", "result": result.scalar()}
