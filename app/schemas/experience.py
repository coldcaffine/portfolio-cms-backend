from pydantic import BaseModel


class ExperienceBase(BaseModel):
    role: str
    company: str | None = None
    description: str | None = None
    start_date: str | None = None
    end_date: str | None = None


class ExperienceCreate(ExperienceBase):
    pass


class ExperienceUpdate(ExperienceBase):
    pass


class ExperienceResponse(ExperienceBase):
    id: int

    class Config:
        from_attributes = True
