from pydantic import BaseModel


class ServiceBase(BaseModel):
    title: str
    description: str | None = None
    icon: str | None = None


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(ServiceBase):
    pass


class ServiceResponse(ServiceBase):
    id: int

    class Config:
        from_attributes = True
