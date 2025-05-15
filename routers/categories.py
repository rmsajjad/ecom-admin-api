from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
import models, schemas
from database import get_session

router = APIRouter()

@router.get("/category")
def retrieve_all_categories(session: Session = Depends(get_session)):
    return session.query(models.Product).all()

@router.post("/category", status_code = status.HTTP_201_CREATED)
def add_category(category: schemas.Category, session: Session = Depends(get_session)):
    categoryObj = models.Category(category=category.category)
    session.add(categoryObj)
    session.commit()
    return {"message": "New category added successfully"}

@router.put("/category")
def update_category(category: schemas.Category, session: Session = Depends(get_session)):
    categoryObj = session.query(models.Category).filter(models.Category.category == category.category).first()
    if not categoryObj:
        raise HTTPException(status_code=404, detail="Category not present")
    categoryObj.category = category.new_category
    session.commit()
    return {"message": "Category updated successfully"}
