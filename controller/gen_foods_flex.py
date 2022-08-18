from utils import *

def gen_foods_carousel(food_data: list):
    bubblelist = []
    for food in food_data:
        bubble = {
            "type": "bubble",
            "size": "kilo",
            "hero": {
                "type": "image",
                "url": food["img_url"],
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": food["food_name"],
                        "weight": "bold",
                        "margin": "md",
                        "flex": 0,
                        "size": "xl"
                    },
                    {
                        "type": "text",
                        "size": "lg",
                        "align": "end",
                        "color": "#aaaaaa",
                        "text": f"฿{food['price']}"
                    }
                    ]
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#4fc3f7",
                        "margin": "sm",
                        "action": {
                        "type": "message",
                        "label": "Add to Cart",
                        "text": food["food_name"]
                        }
                    }
                ]
            }
        }
        
        bubblelist.append(bubble)

    carousel = {
    "type": "carousel",
    "contents": bubblelist
    }
    return flex_message(carousel)

def gen_foods_flexs(food_data: list):
    data_lenght = len(food_data)
    print(data_lenght)
    flexs = []
    start = 0
    while start < data_lenght:
        stop = start + 8 # สร้าง carousel ที่ด้านในมี bubble ไม่เกิด 8 อัน
        if stop > data_lenght - 1:
            stop = data_lenght
        flexs.append(gen_foods_carousel(food_data[start:stop]))
        start = stop
    return flexs