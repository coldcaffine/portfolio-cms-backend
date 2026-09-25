from pydantic import BaseModel


class TestimonialBase(BaseModel):
    name: str
    role: str | None = None
    content: str
    image_url: str | None = None


class TestimonialCreate(TestimonialBase):
    pass


class TestimonialUpdate(TestimonialBase):
    pass


class TestimonialResponse(TestimonialBase):
    id: int

    class Config:
        from_attributes = True
