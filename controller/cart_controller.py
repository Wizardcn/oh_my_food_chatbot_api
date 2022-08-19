from repositories import *

def add_food_on_customer_cart(customer_id: str, food_name: str, amount: int):
    

    food_result = query_with_food_name(food_name)
    cart_result = query_cart(customer_id)
    
    if 200 in food_result:
        food = food_result[200]
        food_id = food["food_id"]
        

        if 200 in cart_result:
            customer_cart = cart_result[200]
            customer_cart["cart"].append({"food_id": food_id, "amount": amount})

            return update_cart(customer_id, customer_cart)
        else:
            return cart_result
    else:
        return food_result