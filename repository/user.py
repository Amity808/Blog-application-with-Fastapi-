from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, hashing


def create_newuser(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show_by_id(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'The user with the {id} is not found')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the {id} not found'}
    return user
