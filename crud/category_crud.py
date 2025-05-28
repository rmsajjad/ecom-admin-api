from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

def get_all_categories(skip: int, limit: int, session: Session):
    return session.query(models.CategoryModel).offset(skip).limit(limit).all()

def create_category(category: schemas.CategoryUpdate, session: Session):
    new_category = models.CategoryModel(category=category.category)
    session.add(new_category)
    session.commit()
    
    return {"message": "New category added successfully"}

def update_category(category: schemas.CategoryUpdate, session: Session):
    category_obj = session.query(models.CategoryModel).filter(models.CategoryModel.category == category.category).first()
    if not category_obj:
        raise HTTPException(status_code=404, detail="Category not present")
    category_obj.category= category.new_category
    session.commit()
    
    return {"message":"Category updated successfully"}
