from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
import schemas, database, models
from sqlalchemy.orm import Session
from repository import blog
from . import oauth2
router = APIRouter()
get_db = database.get_db


@router.get('', status_code=status.HTTP_200_OK, response_model=List[schemas.showBlog])
def get_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


# creating a data users
@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.Blog)
def create(request: schemas.Blog, db: Session = Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create_a_blog(request, db)


# to delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def Delete(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete_by_id(id, db)


# we are having issues with the update records
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    user_id = 1
    message = blog.update(id, request, db, user_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} not found')
    return {"details": "Successfully update details"}


# TO RETRIEVE A BLOG
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.showBlog)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_by_id(id, db)
