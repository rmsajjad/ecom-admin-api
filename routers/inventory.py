from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from crud import inventory_crud
import models, schemas
from database import get_session

router = APIRouter()

@router.get("/inventory/", response_model = List[schemas.InventoryOut])
def get_inventory_info(skip: int = 0, limit: int = 10,session: Session = Depends(get_session)):
    return inventory_crud.get_all_inventory(skip, limit, session)

@router.get("/inventory/{product_id}", response_model = schemas.InventoryOut)
def get_inventory(product_id: int, session: Session = Depends(get_session)):
    return inventory_crud.get_inventory_by_product_id(product_id, session)

@router.put("/inventory/", response_model = schemas.MessageResponse)
def update_inventory(product: schemas.InventoryUpdate, session: Session = Depends(get_session)):
    return inventory_crud.update_inventory_quantity(product, session)