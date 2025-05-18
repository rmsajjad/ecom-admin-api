from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
import models, schemas
from database import get_session

router = APIRouter()

@router.post("/sales-states", status_code = status.HTTP_201_CREATED)
def retrieve_sales_states(saleFilter: schemas.SaleFilter, session: Session = Depends(get_session)):
    query = session.query(models.Sale, models.Product).join(models.Product)
    if saleFilter.start_date:
        query = query.filter(models.Sale.order_date >= datetime.fromisoformat(saleFilter.start_date))
    if saleFilter.end_date:
        query = query.filter(models.Sale.order_date <= datetime.fromisoformat(saleFilter.end_date))    
    if saleFilter.product_id:
        query = query.filter(models.Sale.product_id == saleFilter.product_id)
    if saleFilter.category:
        query = query.filter(models.Product.category == saleFilter.category)

    sale_states = query.order_by(models.email).all()
    result = []
    for sale, product in sale_states:
        result.append({
            "product_name": product.name,
            "product_category": product.category,
            "sale_quantity": sale.quantity,
            "total_price": sale.total_price,
            "sell_date": sale.order_date
        })
    return result

@router.get("/revenue")
def revenue_report(period: str = "daily", days: int = 30, session: Session = Depends(get_session)):
    now = datetime.now()
    duration = {
        "daily": now - timedelta(days=1),
        "weekly": now - timedelta(weeks=1),
        "monthly": now - timedelta(days=30),
        "yearly": now - timedelta(days=365),
        "x_days": now - timedelta(days=days)
    }

    if period not in duration:
        raise HTTPException(status_code=400, detail="Invalid period. Choose from daily, weekly, monthly, yearly.")

    start = duration[period]
    revenue = session.query(func.sum(models.Sale.total_price)).filter(models.Sale.order_date >= start).scalar()
    return {"Period": period, "Revenue": revenue or 0.0}
