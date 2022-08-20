from sqlite3 import Timestamp
from pydantic import BaseModel

class Order(BaseModel):
    order_id: str # auto gen mongodb
    customer_id: str
    display_name: str
    timestamp: str # generate by our API in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm)
    cart: list
    
    class Config:
        schema_extra = {
            "example": {
                "order_id": "212334214",
                "customer_id": "U45029b0ec683201a3b77414534d3d7a9",
                "display_name": "อาท",
                "timestamp": "21/02/2022",
                "cart": [
                                    {"food_id": "food00001", "amount": 5},
                                    {"food_id": "food00003", "amount": 4}
                                ]
            }
        }
        
class AddOrderRequestBody(BaseModel):
    customer_id: str
    display_name: str
    
    class Config:
        schema_extra = {
            "example": {
                "customer_id": "U45029b0ec683201a3b77414534dsd7a9",
                "display_name": "อาท"
            }
        }