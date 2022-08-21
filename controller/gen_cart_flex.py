from repositories.food_repo import query_with_food_id
from utils import *


def total_price(cart_data):
    
    total_price = 0
    for item in cart_data:
        result = query_with_food_id([item["food_id"]])
        food = result[200][0]
        total_price += food["price"] * item["amount"]
    
    return total_price

def total_amount(cart_data):
    
    result = 0
    for item in cart_data:
        result += item["amount"]
        
    return result


def gen_cart_flex(cart_data) -> dict:
    
    product_list = []
    
    for item in cart_data:
        result = query_with_food_id([item["food_id"]])
        food = result[200][0]
    
        product = {
            "borderWidth": "none",
            "contents": [
            {
                "aspectMode": "fit",
                "flex": 1,
                "margin": "none",
                "size": "full",
                "type": "image",
                "url": food["img_url"]
            },
            {
                "borderWidth": "none",
                "contents": [
                {
                    "align": "start",
                    "color": "#0c090a",
                    "decoration": "none",
                    "margin": "none",
                    "offsetStart": "xs",
                    "position": "relative",
                    "size": "md",
                    "style": "normal",
                    "text": food["food_name"],
                    "type": "text",
                    "weight": "bold",
                    "wrap": True
                }
                ],
                "flex": 3,
                "layout": "vertical",
                "margin": "none",
                "offsetStart": "xxl",
                "spacing": "none",
                "type": "box"
            },
            {
                "borderWidth": "bold",
                "contents": [
                {
                    "align": "end",
                    "color": "#757c88",
                    "margin": "none",
                    "size": "md",
                    "text": f"x{item['amount']}",
                    "type": "text"
                },
                {
                    "align": "end",
                    "color": "#757c88",
                    "text": f"฿{food['price']}",
                    "type": "text"
                }
                ],
                "flex": 1,
                "layout": "vertical",
                "margin": "none",
                "paddingEnd": "xs",
                "spacing": "xs",
                "type": "box"
            }
            ],
            "cornerRadius": "none",
            "layout": "horizontal",
            "margin": "lg",
            "offsetEnd": "none",
            "paddingEnd": "none",
            "spacing": "sm",
            "type": "box"
        }
    
        product_list.append(product)
    
    product_box = {
        "type": "box",
        "layout": "vertical",
        "contents": product_list
    }
    
    bubble = {
        "type": "bubble",
        "size": "mega",
        "body": {
        "contents": [
            {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "color": "#757c88",
                "size": "lg",
                "text": f"ตะกร้าสินค้า: {total_amount(cart_data)} ชิ้น",
                "type": "text",
                "weight": "bold"
                }
            ]
            },
            product_box,
            {
            "contents": [
                {
                "color": "#757c88",
                "flex": 2,
                "size": "lg",
                "text": "รวมราคาทั้งหมด",
                "type": "text",
                "weight": "bold",
                "wrap": True
                },
                {
                "align": "end",
                "color": "#757c88",
                "size": "md",
                "text": f"฿{total_price(cart_data):.2f}",
                "type": "text",
                "weight": "bold",
                "wrap": True
                }
            ],
            "layout": "horizontal",
            "offsetTop": "xl",
            "spacing": "none",
            "type": "box",
            "borderWidth": "semi-bold"
            }
        ],
        "layout": "vertical",
        "type": "box"
        },
        "footer": {
        "contents": [
            {
            "action": {
                "type": "postback",
                "label": "Confirm",
                "data": "cart_confirm_order"
            },
            "height": "sm",
            "style": "primary",
            "type": "button",
            "color": "#4fc3f7"
            }
        ],
        "flex": 0,
        "layout": "vertical",
        "spacing": "sm",
        "type": "box"
        }
    }
    
    return flex_message(bubble)