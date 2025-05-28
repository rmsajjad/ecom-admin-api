from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from crud import sales_crud
import schemas
from database import get_session

router = APIRouter()

@router.post("/sales-states", response_model = List[dict])
def retrieve_sales_states(saleFilter: schemas.SaleFilter,skip: int = 0, limit: int = 10, 
                          session: Session = Depends(get_session)):
     return sales_crud.get_sales_statistics(saleFilter, skip, limit, session)

@router.get("/revenue", response_model = dict)
def revenue_report(period: str = "daily", days: int = 1, session: Session = Depends(get_session)):
    try:
        return sales_crud.get_revenue_report(period, days, session)
    except ValueError as ve:
        raise HTTPException(status_code = 400, detail = str(ve))
