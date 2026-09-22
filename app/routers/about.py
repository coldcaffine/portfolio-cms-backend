from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.about import About
from app.schemas.about import AboutCreate, AboutUpdate, AboutResponse
from app.core.deps import get_current_user

router = APIRouter(prefix="/about", tags=["About"])


@router.post("/", response_model=AboutResponse)
def create_about(
    about: AboutCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    db_about = About(**about.model_dump())
    db.add(db_about)
    db.commit()
    db.refresh(db_about)
    return db_about


@router.get("/", response_model=AboutResponse)
def get_about(db: Session = Depends(get_db)):
    about = db.query(About).first()

    if not about:
        raise HTTPException(status_code=404, detail="About information not found")

    return about


@router.put("/{about_id}", response_model=AboutResponse)
def update_about(
    about_id: int,
    about: AboutUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    db_about = db.query(About).filter(About.id == about_id).first()

    if not db_about:
        raise HTTPException(status_code=404, detail="About information not found")

    for key, value in about.model_dump().items():
        setattr(db_about, key, value)

    db.commit()
    db.refresh(db_about)

    return db_about


@router.delete("/{about_id}")
def delete_about(
    about_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    db_about = db.query(About).filter(About.id == about_id).first()

    if not db_about:
        raise HTTPException(status_code=404, detail="About information not found")

    db.delete(db_about)
    db.commit()

    return {"message": "About information deleted successfully"}
