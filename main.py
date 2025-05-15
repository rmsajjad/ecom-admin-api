from fastapi import FastAPI
from database import Base, engine
from routers import categories, products, inventory, sales

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(categories.router)
app.include_router(products.router)
app.include_router(inventory.router)
app.include_router(sales.router)
