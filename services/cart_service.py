from fastapi import APIRouter, status, HTTPException
from controller import add_food_on_customer_cart
from models.error_model import DatabaseError
from models.cart_model import AddFoodRequestBody, Cart


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