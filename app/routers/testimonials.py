from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.testimonial import Testimonial
from app.schemas.testimonial import (
    TestimonialCreate,
    TestimonialUpdate,
    TestimonialResponse,
)
from app.core.deps import get_current_user


router = APIRouter(
    prefix="/testimonials",
    tags=["Testimonials"]
)


@router.get("/", response_model=list[TestimonialResponse])
def get_testimonials(
    db: Session = Depends(get_db)
):
    return db.query(Testimonial).all()


@router.post("/", response_model=TestimonialResponse)
def create_testimonial(
    testimonial: TestimonialCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_testimonial = Testimonial(
        name=testimonial.name,
        role=testimonial.role,
        content=testimonial.content,
        image_url=testimonial.image_url,
    )

    db.add(new_testimonial)
    db.commit()
    db.refresh(new_testimonial)

    return new_testimonial


@router.put("/{testimonial_id}", response_model=TestimonialResponse)
def update_testimonial(
    testimonial_id: int,
    testimonial: TestimonialUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing_testimonial = (
        db.query(Testimonial)
        .filter(Testimonial.id == testimonial_id)
        .first()
    )

    if not existing_testimonial:
        raise HTTPException(
            status_code=404,
            detail="Testimonial not found"
        )

    existing_testimonial.name = testimonial.name
    existing_testimonial.role = testimonial.role
    existing_testimonial.content = testimonial.content
    existing_testimonial.image_url = testimonial.image_url

    db.commit()
    db.refresh(existing_testimonial)

    return existing_testimonial


@router.delete("/{testimonial_id}")
def delete_testimonial(
    testimonial_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing_testimonial = (
        db.query(Testimonial)
        .filter(Testimonial.id == testimonial_id)
        .first()
    )

    if not existing_testimonial:
        raise HTTPException(
            status_code=404,
            detail="Testimonial not found"
        )

    db.delete(existing_testimonial)
    db.commit()

    return {"message": "Testimonial deleted successfully"}
