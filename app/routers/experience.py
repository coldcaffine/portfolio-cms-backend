from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.experience import Experience
from app.schemas.experience import (
    ExperienceCreate,
    ExperienceUpdate,
    ExperienceResponse,
)
from app.core.deps import get_current_user


router = APIRouter(
    prefix="/experience",
    tags=["Experience"]
)


@router.get("/", response_model=list[ExperienceResponse])
def get_experiences(
    db: Session = Depends(get_db)
):
    return db.query(Experience).all()


@router.post("/", response_model=ExperienceResponse)
def create_experience(
    experience: ExperienceCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_experience = Experience(
        role=experience.role,
        company=experience.company,
        description=experience.description,
        start_date=experience.start_date,
        end_date=experience.end_date,
    )

    db.add(new_experience)
    db.commit()
    db.refresh(new_experience)

    return new_experience


@router.put("/{experience_id}", response_model=ExperienceResponse)
def update_experience(
    experience_id: int,
    experience: ExperienceUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing_experience = (
        db.query(Experience)
        .filter(Experience.id == experience_id)
        .first()
    )

    if not existing_experience:
        raise HTTPException(
            status_code=404,
            detail="Experience not found"
        )

    existing_experience.role = experience.role
    existing_experience.company = experience.company
    existing_experience.description = experience.description
    existing_experience.start_date = experience.start_date
    existing_experience.end_date = experience.end_date

    db.commit()
    db.refresh(existing_experience)

    return existing_experience


@router.delete("/{experience_id}")
def delete_experience(
    experience_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing_experience = (
        db.query(Experience)
        .filter(Experience.id == experience_id)
        .first()
    )

    if not existing_experience:
        raise HTTPException(
            status_code=404,
            detail="Experience not found"
        )

    db.delete(existing_experience)
    db.commit()

    return {"message": "Experience deleted successfully"}
