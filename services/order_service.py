from fastapi import APIRouter, status, HTTPException
from controller import *
from models import *
from utils import *


order_router = APIRouter(tags=["orders"])

@order_router.post("/", status_code=status.HTTP_201_CREATED, 
                            responses={
                                201: {
                                    "model": Order,
                                    "description": "Order Was Created"
                                },
                                520: {
                                    'model': DatabaseError,
                                    'description': 'Database Connection Error'
                                }
                            })
async def create_customer_order(body: AddOrderRequestBody):
    
    body = dict(body)
    customer_id = body["customer_id"]
    display_name = body["display_name"]

    
    result = summarize_customer_order(customer_id, display_name)

    if 201 in result:
        return result[201]
    else:
        error_key = list(result.keys())[0]
        raise HTTPException(status_code=error_key, detail=result[error_key])