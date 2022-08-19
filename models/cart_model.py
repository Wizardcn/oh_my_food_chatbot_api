from lib2to3.pytree import Base
from pydantic import BaseModel

class Cart(BaseModel):
    customer_id: str
    cart: list

    class Config:
        scheme_extra = {
            "example": {
                "customer_id": "U45029b0ec683201a3b77414534d3d7a9",
                "cart": [
                            {"food_id": "food00001", "amount": 5},
                            {"food_id": "food00003", "amount": 4}
                ]
            }
        }

class AddFoodRequestBody(BaseModel):
    customer_id: str
    food_name: str
    amount: int
    
    class Config: 
        schema_extra = {
            "example": {
                "customer_id": "U45029b0ec683201a3b77414534d3d7a9",
                "food_name": "ปลาดิบ",
                "amount": 5
            }
        }