from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from crud import category_crud
from database import get_session
from schemas import CategoryIn, CategoryOut,MessageResponse,CategoryUpdate

router = APIRouter()

"""
Get a single item by ID

- **item_id**: The ID of the item
- **q**: Optional search filter
"""
@router.get("/category", response_model = List[CategoryOut])
def retrieve_all_categories(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
     return category_crud.get_all_categories(skip, limit, session)

@router.post("/category", response_model = MessageResponse, status_code = status.HTTP_201_CREATED)
def add_category(category: CategoryIn, session: Session = Depends(get_session)):
    return category_crud.create_category(category, session)

@router.put("/category", response_model = MessageResponse)
def update_category(category: CategoryUpdate, session: Session = Depends(get_session)):
    return category_crud.update_category(category, session)
