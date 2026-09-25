from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.blog import Blog
from app.schemas.blog import BlogCreate, BlogUpdate, BlogResponse
from app.core.deps import get_current_user


router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)


@router.get("/", response_model=list[BlogResponse])
def get_blogs(
    db: Session = Depends(get_db)
):
    return db.query(Blog).all()


@router.post("/", response_model=BlogResponse)
def create_blog(
    blog: BlogCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_blog = Blog(
        title=blog.title,
        content=blog.content,
        excerpt=blog.excerpt,
        cover_image=blog.cover_image,
        published=blog.published
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


@router.put("/{blog_id}", response_model=BlogResponse)
def update_blog(
    blog_id: int,
    blog: BlogUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing_blog = (
        db.query(Blog)
        .filter(Blog.id == blog_id)
        .first()
    )

    if not existing_blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    existing_blog.title = blog.title
    existing_blog.content = blog.content
    existing_blog.excerpt = blog.excerpt
    existing_blog.cover_image = blog.cover_image
    existing_blog.published = blog.published

    db.commit()
    db.refresh(existing_blog)

    return existing_blog


@router.delete("/{blog_id}")
def delete_blog(
    blog_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing_blog = (
        db.query(Blog)
        .filter(Blog.id == blog_id)
        .first()
    )

    if not existing_blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    db.delete(existing_blog)
    db.commit()

    return {"message": "Blog deleted successfully"}
