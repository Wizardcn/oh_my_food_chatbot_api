from fastapi import APIRouter, status, HTTPException
from models.error_model import DatabaseError, FoodNotFoundError
from models.food_model import FoodFlex, FoodIdRequestBody
from repositories.food_repo import query_with_food_id
from controller import *
from utils.payload import *

food_router = APIRouter(tags=["foods"])

@food_router.post("/", status_code=status.HTTP_200_OK, 
                         responses={
                             200: {
                                 "model": FoodFlex,
                             },
                             520: {
                                'model': DatabaseError,
                                'description': 'Database Connection Error'
                             }
                         })
async def get_foods_flexs_by_food_id(food_id_request_body: FoodIdRequestBody):
    
    food_id_list = dict(food_id_request_body)["food_id_list"]
    
    result = query_with_food_id(food_id_list)
    if 200 in result:
        food_data = result[200]
        foods_flex = gen_foods_flexs(food_data)
        return botnoi_payload(foods_flex)
    elif 404 in result:
        return botnoi_payload(text_message(["ไม่พบสินค้าในระบบนะครับ"]))
    else:
        error_key = list(result.keys())[0]
        raise HTTPException(status_code=error_key, detail=result[error_key])
    
    
@food_router.get("/{category}", status_code=status.HTTP_200_OK, responses={
                             200: {
                                 "model": FoodFlex,
                             },
                             520: {
                                'model': DatabaseError,
                                'description': 'Database Connection Error'
                             }
                         })
async def get_foods_flexs_by_category(category: str):
    
    result = query_with_food_category(category)
    
    if 200 in result:
        food_data = result[200]
        foods_flex = gen_foods_flexs(food_data)
        return botnoi_payload(foods_flex)
    elif 404 in result:
        return botnoi_payload(text_message(["ไม่พบสินค้าในระบบนะครับ"]))
    else:
        error_key = list(result.keys())[0]
        raise HTTPException(status_code=error_key, detail=result[error_key])
    
    