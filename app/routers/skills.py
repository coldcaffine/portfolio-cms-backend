from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillUpdate, SkillResponse
from app.core.deps import get_current_user


router = APIRouter(
    prefix="/skills",
    tags=["Skills"]
)


@router.get("/", response_model=list[SkillResponse])
def get_skills(
    db: Session = Depends(get_db)
):
    return db.query(Skill).all()


@router.post("/", response_model=SkillResponse)
def create_skill(
    skill: SkillCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_skill = Skill(
        name=skill.name,
        category=skill.category,
        level=skill.level
    )

    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)

    return new_skill


@router.put("/{skill_id}", response_model=SkillResponse)
def update_skill(
    skill_id: int,
    skill: SkillUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing_skill = db.query(Skill).filter(Skill.id == skill_id).first()

    if not existing_skill:
        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    existing_skill.name = skill.name
    existing_skill.category = skill.category
    existing_skill.level = skill.level

    db.commit()
    db.refresh(existing_skill)

    return existing_skill


@router.delete("/{skill_id}")
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing_skill = db.query(Skill).filter(Skill.id == skill_id).first()

    if not existing_skill:
        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    db.delete(existing_skill)
    db.commit()

    return {"message": "Skill deleted successfully"}
