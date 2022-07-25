from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create_a_blog(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete_by_id(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Blog, db: Session, user_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        return 0
    request.__dict__.update(user_id=user_id)
    blog.update(request.__dict__)
    db.commit()
    return "update"


def get_by_id(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'The blog with the {id} is not found')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the {id} not found'}
    return blog
