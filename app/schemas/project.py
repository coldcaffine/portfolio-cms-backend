from pydantic import BaseModel


class ProjectBase(BaseModel):
    title: str
    description: str | None = None
    tech_stack: str | None = None
    github_url: str | None = None
    live_url: str | None = None
    image_url: str | None = None


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass


class ProjectResponse(ProjectBase):
    id: int

    class Config:
        from_attributes = True
