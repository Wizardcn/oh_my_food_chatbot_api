from repositories import *
import datetime

def summarize_customer_order(customer_id: str, display_name: str):
    
    cart_result = query_cart(customer_id)
    
    if 200 in cart_result:
        customer_cart = cart_result[200]
        cart_data = customer_cart["cart"]
        
        timestamp = str(datetime.datetime.now())
        
        create_order_result = create_order(customer_id, display_name, timestamp, cart_data)
        
        if 201 in create_order_result:
            customer_cart["cart"] = [] # clear customer cart after create new order from that cart
            update_cart(customer_id, customer_cart)
            return {201: create_order_result[201]}
        else:
            return create_order_result
    else: 
        return cart_result