from sqlalchemy import Column, Integer, String,Float, DateTime, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Product(Base):
    __tablename__ = 'categories'
    id = Column(Integer, index = True)
    category = Column(String(50), primary_key=True, nullable = False)
   
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index = True)
    name = Column(String(50), nullable = False)
    description = Column(String(255), nullable = False)
    price = Column(Float, nullable = False)
    category = Column(String(50),ForeignKey("categories.category"))
    inventory = relationship("Inventory", back_populates="product", uselist=False)

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    stock_level = Column(Integer, default=0)
    last_updated_at = Column(DateTime(timezone=True), default=func.now())
    product = relationship("Product", back_populates="inventory")

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable = False)
    total_price = Column(Float, nullable = False)
    order_date = Column(DateTime(timezone=True), index=True)


    