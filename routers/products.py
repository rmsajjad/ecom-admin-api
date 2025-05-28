from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from crud import product_crud
from schemas import Product,ProductOut,MessageResponse
from database import get_session
import crud

router = APIRouter()

@router.get("/product", response_model = List[ProductOut])
def retrieve_all_products(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    return product_crud.get_all_products(skip, limit, session)

@router.get("/product/{product_id}", response_model = ProductOut)
def retrieve_product(product_id: int, session: Session = Depends(get_session)):
    return product_crud.get_product_by_id(product_id, session)

@router.post("/product", response_model = MessageResponse, status_code = status.HTTP_201_CREATED)
def create_new_product(product: Product, session: Session = Depends(get_session)):
    return product_crud.create_product(product, session)