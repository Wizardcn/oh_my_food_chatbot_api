def food_serializer(food) -> dict:
    
    return {
        "food_id": str(food["food_id"]),
        "food_name": str(food["food_name"]),
        "img_url": str(food["img_url"]),
        "price": int(food["price"])
    }

def foods_serializer(foods) -> list:
    return [food_serializer(food) for food in foods]