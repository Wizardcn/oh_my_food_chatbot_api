from fastapi import APIRouter, status, HTTPException
from models.error_model import DatabaseError, FoodNotFoundError
from models.food_model import Food, FoodIdRequestBody
from repositories.food_repo import query_with_food_id
from controller import *
from utils.payload import *

food_router = APIRouter(tags=["foods"])

@food_router.post("/", status_code=status.HTTP_201_CREATED, 
                         responses={
                             201: {
                                 "model": Food
                             },
                             404: {
                                 "model": FoodNotFoundError,
                                 "description": "Food Not Found Error"
                             },
                             520: {
                                'model': DatabaseError,
                                'description': 'Database Connection Error'
                             }
                         })
async def get_foods_flex(food_id_request_body: FoodIdRequestBody):
    
    food_id_list = dict(food_id_request_body)["food_id_list"]
    
    result = query_with_food_id(food_id_list)
    if 200 in result:
        food_data = result[200]
        foods_flex = gen_foods_flexs(food_data)
        return botnoi_payload(foods_flex)
    
    else:
        error_key = list(result.keys())[0]
        raise HTTPException(status_code=error_key, detail=result[error_key])
    

    
# from controller import gen_foods_carousel
# from dbconnector import Mongoatlas
# from utils.payload import *
# import json
# foods_col = Mongoatlas(collection="foods")
# food_data = foods_col.find({})["documents"][:4]
# print(json.dumps(gen_foods_carousel(food_data)))