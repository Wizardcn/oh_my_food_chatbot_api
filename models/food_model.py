from pydantic import BaseModel

class Food(BaseModel):
    food_id: str
    food_name: str
    img_url: str
    price: int
    
    class Config:
        schema_extra = {
            "example": {
                "food_id":"food00009",
                "food_name": "ก๋วยเตี๋ยวคั่วไก่", 
                "img_url":"https://food.mthai.com/app/uploads/2017/12/Kua-Gai.jpg",
                "price":60,
            }
        }
        
        
class FoodIdRequestBody(BaseModel):
    food_id_list: list
    
    class Config:
        schema_extra = {
            "example": {
                "food_id_list": ["food00001", "food00023"]
            }
        }