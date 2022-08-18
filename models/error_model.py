from pydantic import BaseModel


class UserNotFoundError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "User with the customer_i is not available"},
        }
        
        
class FoodNotFoundError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "Food with the food_id is not available"},
        }
        
        
class DatabaseError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "Fail to connect Database"},
        }
        
# class FoodNotMatchError(BaseModel):
#     detail: str
    
#     class Config:
#         schema_extra = {
#             "example": {"detail": "Food with the food_id is no document matches"}
#         }