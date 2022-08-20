from fastapi import APIRouter, status, HTTPException
from controller import *
from controller.recommender import recommend_food_by_knowledges
from models import *
from utils import *


recommender_router = APIRouter(tags=["recommenders"])

@recommender_router.get("/knowledges", status_code=status.HTTP_200_OK, 
                         responses={
                             200: {
                                 "model": FoodFlex,
                             },
                             520: {
                                'model': DatabaseError,
                                'description': 'Database Connection Error'
                             }
                         })
async def recommend_foods_with_knowledges(sub_topic: str):
    
    result = recommend_food_by_knowledges(sub_topic)
    
    if 200 in result:
        food_data = result[200]
        foods_flex = gen_foods_flexs(food_data)
        return botnoi_payload(foods_flex)
    elif 404 in result:
        return botnoi_payload(text_message(["หัวข้อนี้เรายังแนะนำไม่ได้นะครับ 🙏😔"]))
    else:
        error_key = list(result.keys())[0]
        raise HTTPException(status_code=error_key, detail=result[error_key])