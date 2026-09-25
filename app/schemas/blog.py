from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    content: str
    excerpt: str | None = None
    cover_image: str | None = None
    published: str | None = None


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BlogBase):
    pass


class BlogResponse(BlogBase):
    id: int

    class Config:
        from_attributes = True
