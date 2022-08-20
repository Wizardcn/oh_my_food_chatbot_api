from repositories import *

def recommend_food_by_knowledges(sub_topic: str):
    
    knowledges_result = query_knowledges_with_sub_topic(sub_topic)
    
    if 200 in knowledges_result:
        food_id_list = knowledges_result[200]["food_list"]
        
        return query_with_food_id(food_id_list)
    else:
        return knowledges_result
 