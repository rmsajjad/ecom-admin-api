from sqlalchemy import Column, Integer, String,Float, DateTime, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class CategoryModel(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(50), unique=True, nullable=False)
   
class ProductModel(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index = True)
    name = Column(String(50), nullable = False)
    description = Column(String(255), nullable = False)
    price = Column(Float, nullable = False)
    category = Column(String(50), ForeignKey("categories.category"), nullable=False)
    inventory = relationship("InventoryModel", back_populates="product")
  
class InventoryModel(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    stock_level = Column(Integer, default=0)
    last_updated_at = Column(DateTime(timezone=True), default=func.now())
    product = relationship("ProductModel", back_populates="inventory")
  
class SaleModel(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable = False)
    total_price = Column(Float, nullable = False)
    order_date = Column(DateTime(timezone=True), index=True)
  

    