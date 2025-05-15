from pydantic import BaseModel
from datetime import datetime

class Category(BaseModel):
    category : str

class ProductDetail(BaseModel):
    name: str
    category : str
    description : str
    price: float
    quantity: int | None = None

class InventoryUpdate(BaseModel):
    product_id: int
    quantity: int | None = None

class SaleFilter(BaseModel):
    start_date: datetime | None = None
    end_date: datetime | None = None
    category: str | None = None
    product_id: int | None = None