from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import database
import schemas
from repository import user

router = APIRouter()
get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.Usershow)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_newuser(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show(id, db: Session = Depends(get_db)):
    return user.show_by_id(id, db)
