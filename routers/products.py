from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
import models, schemas
from database import get_session

router = APIRouter()

@router.get("/product")
def retrieve_all_product_information(session: Session = Depends(get_session)):
    return session.query(models.Product).all()

@router.get("/product/{product_id}")
def get_inventory(product_id: int, session: Session = Depends(get_session)):
    product = session.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/product", status_code = status.HTTP_201_CREATED)
def add_product(product: schemas.ProductDetail, session: Session = Depends(get_session)):
    product_detail = models.Product(
        name=product.name, 
        category=product.category, 
        description=product.description, 
        price=product.price
    )
    session.add(product_detail)
    session.commit()
    session.refresh(product_detail)

    inventory_detail = models.Inventory(product_id=product_detail.id, stock_level=product.quantity)
    session.add(inventory_detail)
    session.commit()
    return {"message": "Product registered successfully"}
