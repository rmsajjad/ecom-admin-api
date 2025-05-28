from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import models, schemas

#Proudct CRUD operation
def get_all_products(skip: int, limit: int, session: Session):
    return session.query(models.ProductModel).offset(skip).limit(limit).all()

def get_product_by_id(product_id: int, session: Session):
    product = session.query(models.ProductModel).filter(models.ProductModel.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def create_product(product_data: schemas.Product, session: Session):
    data = product_data.model_dump()
    data.pop("quantity", None)  #remove quantity if present
    
    product = models.ProductModel(**data)
    session.add(product)
    session.flush()  # Get ID before commit

    inventory = models.InventoryModel(product_id=product.id, stock_level=product_data.quantity)
    session.add(inventory)
    session.commit()

    return {"message": "Product registered successfully"}