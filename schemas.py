from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class CategoryIn(BaseModel):
    category: str

class CategoryOut(BaseModel):
    id: Optional[int]
    category: str

class CategoryUpdate(BaseModel):
    category: str
    new_category: str

class Product(BaseModel):
    name: str
    category: str
    description: str
    price: float
    quantity: int | None = None

class ProductOut(BaseModel):
    id: int
    name: str
    category: str
    description: str
    price: float


class InventoryOut(BaseModel):
    id: int
    product_id: int
    stock_level: int
    last_updated_at: datetime
    
class InventoryUpdate(BaseModel):
    product_id: int
    quantity: int | None = None

class SaleFilter(BaseModel):
    start_date: datetime | None = None
    end_date: datetime | None = None
    category: str | None = None
    product_id: int | None = None

#Response
class MessageResponse(BaseModel):
    message: str
