from fastapi import APIRouter, status, HTTPException
from controller import *
from models.error_model import DatabaseError
from models.cart_model import AddFoodRequestBody, Cart
from repositories.cart_repo import query_cart
from utils import *


cart_router = APIRouter(tags=["carts"])

@cart_router.put("/", status_code=status.HTTP_200_OK, 
                            responses={
                                200: {
                                    "model": Cart,
                                    "description": "Cart Was Updated"
                                },
                                520: {
                                    'model': DatabaseError,
                                    'description': 'Database Connection Error'
                                }
                            })
async def add_food_to_cart(body: AddFoodRequestBody):
    
    body = dict(body)
    customer_id = str(body["customer_id"])
    food_name = str(body["food_name"])
    amount = int(body["amount"])
    
    result = add_food_on_customer_cart(customer_id, food_name, amount)

    if 200 in result:
        return result[200]
    else:
        error_key = list(result.keys())[0]
        raise HTTPException(status_code=error_key, detail=result[error_key])
    
    
@cart_router.get("/{customer_id}", status_code=status.HTTP_200_OK, 
                         responses={
                             200: {
                                 "model": CartFlex,
                             },
                             520: {
                                'model': DatabaseError,
                                'description': 'Database Connection Error'
                             }
                         })
async def get_customer_cart_flex(customer_id: str):
    
    result = query_cart(customer_id)
    
    if 200 in result:
        cart = result[200]
        cart_data = cart["cart"]
        cart_flex = gen_cart_flex(cart_data)
        return botnoi_payload(cart_flex)
    elif 404 in result:
        return botnoi_payload(text_message(["ตอนนี้ลูกค้าไม่มีสินค้าในตะกร้านะครับ", "หากลูกค้าสนใจสั่งสินค้าสามารถกดปุ่มที่เมนูด้านล่างนี้ได้เลยครับ 👇"]))
    else:
        error_key = list(result.keys())[0]
        raise HTTPException(status_code=error_key, detail=result[error_key])