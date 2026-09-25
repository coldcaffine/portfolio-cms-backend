from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from app.core.deps import get_current_user


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.get("/", response_model=list[ProjectResponse])
def get_projects(
    db: Session = Depends(get_db)
):
    return db.query(Project).all()


@router.post("/", response_model=ProjectResponse)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_project = Project(
        title=project.title,
        description=project.description,
        tech_stack=project.tech_stack,
        github_url=project.github_url,
        live_url=project.live_url,
        image_url=project.image_url
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(
    project_id: int,
    project: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing_project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not existing_project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    existing_project.title = project.title
    existing_project.description = project.description
    existing_project.tech_stack = project.tech_stack
    existing_project.github_url = project.github_url
    existing_project.live_url = project.live_url
    existing_project.image_url = project.image_url

    db.commit()
    db.refresh(existing_project)

    return existing_project


@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing_project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not existing_project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    db.delete(existing_project)
    db.commit()

    return {"message": "Project deleted successfully"}
