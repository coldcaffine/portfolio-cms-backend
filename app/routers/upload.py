import os
import shutil
from uuid import uuid4

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.database import get_db
from app.models.media import Media


router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/image")
def upload_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    allowed_types = {
        "image/jpeg",
        "image/png",
        "image/webp",
        "image/gif"
    }

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only JPEG, PNG, WEBP, and GIF images are allowed"
        )

    extension = os.path.splitext(file.filename or "")[1].lower()

    filename = f"{uuid4().hex}{extension}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    file_url = f"/uploads/{filename}"

    media = Media(
        filename=file.filename or filename,
        file_url=file_url,
        file_type=file.content_type
    )

    db.add(media)
    db.commit()
    db.refresh(media)

    return {
        "message": "Image uploaded successfully",
        "id": media.id,
        "filename": media.filename,
        "file_url": media.file_url,
        "file_type": media.file_type
    }
