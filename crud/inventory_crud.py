from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timezone
import models, schemas

def get_all_inventory(skip: int, limit: int, session: Session):
    inventory = session.query(models.InventoryModel).offset(skip).limit(limit).all()
    if not inventory:
        raise HTTPException(status_code=404, detail="Product not available")
    return inventory

def get_inventory_by_product_id(product_id: int, session: Session):
    inventory = session.query(models.InventoryModel).filter(models.InventoryModel.product_id == product_id).first()
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inventory

def update_inventory_quantity(product: schemas.InventoryUpdate, session: Session):
    inventory_data = session.query(models.InventoryModel).filter(models.InventoryModel.product_id == product.product_id).first()
    if not inventory_data:
        raise HTTPException(status_code=404, detail="Product not available")
    
    inventory_data.stock_level = product.quantity
    inventory_data.last_updated_at = datetime.now(timezone.utc)
    session.commit()
    return {"message": "Inventory updated"}
