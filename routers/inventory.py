from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone
import models, schemas
from database import get_session

router = APIRouter()

@router.get("/inventory/")
def get_inventory_info(session: Session = Depends(get_session)):
    inventory_data = session.query(models.Inventory).all()
    if not inventory_data:
        raise HTTPException(status_code=404, detail="Product not available")
    return inventory_data

@router.get("/inventory/{product_id}")
def get_inventory(product_id: int, session: Session = Depends(get_session)):
    inventory = session.query(models.Inventory).filter(models.Inventory.product_id == product_id).first()
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inventory

@router.put("/inventory/")
def update_inventory(product: schemas.InventoryUpdate, session: Session = Depends(get_session)):
    inventory_data = session.query(models.Inventory).filter(models.Inventory.product_id == product.product_id).first()
    if not inventory_data:
        raise HTTPException(status_code=404, detail="Product not available")
    inventory_data.stock_level = product.quantity
    inventory_data.last_updated_at = datetime.now(timezone.utc)
    session.commit()
    return {"message": "Inventory updated"}
