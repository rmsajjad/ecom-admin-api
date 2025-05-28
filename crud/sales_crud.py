from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
import models, schemas

def get_sales_statistics(sale_filter: schemas.SaleFilter, skip: int, limit: int, session: Session):
    query = session.query(models.SaleModel, models.ProductModel).join(models.ProductModel)

    if sale_filter.start_date:
        query = query.filter(models.SaleModel.order_date >= sale_filter.start_date)
    if sale_filter.end_date:
        query = query.filter(models.SaleModel.order_date <= sale_filter.end_date)    
    if sale_filter.product_id:
        query = query.filter(models.SaleModel.product_id == sale_filter.product_id)
    if sale_filter.category:
        query = query.filter(models.ProductModel.category == sale_filter.category)

    sale_records = query.offset(skip).limit(limit).all()
    
    return [
        {
            "product_name": product.name,
            "product_category": product.category,
            "sale_quantity": sale.quantity,
            "total_price": sale.total_price,
            "sell_date": sale.order_date
        }
        for sale, product in sale_records
    ]

def get_revenue_report(period: str, days: int, session: Session):
    now = datetime.now()
    duration = {
        "daily": now - timedelta(days=1),
        "weekly": now - timedelta(weeks=1),
        "monthly": now - timedelta(days=30),
        "yearly": now - timedelta(days=365),
        "x_days": now - timedelta(days=days)
    }

    if period not in duration:
        raise ValueError("Invalid period. Choose from daily, weekly, monthly, yearly,x_days.")

    start_date = duration[period]
    total_revenue = session.query(func.sum(models.SaleModel.total_price)).filter(
        models.SaleModel.order_date >= start_date
    ).scalar()

    return {
        "period": period,
        "till_date": start_date,
        "revenue": total_revenue or 0.0
    }
