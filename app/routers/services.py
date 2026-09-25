from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceUpdate, ServiceResponse
from app.core.deps import get_current_user


router = APIRouter(
    prefix="/services",
    tags=["Services"]
)


@router.get("/", response_model=list[ServiceResponse])
def get_services(
    db: Session = Depends(get_db)
):
    return db.query(Service).all()


@router.post("/", response_model=ServiceResponse)
def create_service(
    service: ServiceCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_service = Service(
        title=service.title,
        description=service.description,
        icon=service.icon
    )

    db.add(new_service)
    db.commit()
    db.refresh(new_service)

    return new_service


@router.put("/{service_id}", response_model=ServiceResponse)
def update_service(
    service_id: int,
    service: ServiceUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing_service = (
        db.query(Service)
        .filter(Service.id == service_id)
        .first()
    )

    if not existing_service:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    existing_service.title = service.title
    existing_service.description = service.description
    existing_service.icon = service.icon

    db.commit()
    db.refresh(existing_service)

    return existing_service


@router.delete("/{service_id}")
def delete_service(
    service_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing_service = (
        db.query(Service)
        .filter(Service.id == service_id)
        .first()
    )

    if not existing_service:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    db.delete(existing_service)
    db.commit()

    return {"message": "Service deleted successfully"}
