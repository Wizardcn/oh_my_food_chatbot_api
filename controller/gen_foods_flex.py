from utils import *

def gen_foods_carousel(food_data: list):
    bubblelist = []
    for food in food_data:
        bubble = {
            "body": {
                "contents": [
                {
                    "size": "xl",
                    "text": food["food_name"],
                    "type": "text",
                    "weight": "bold",
                    "wrap": True
                },
                {
                    "contents": [
                    {
                        "flex": 0,
                        "size": "xl",
                        "text": f"฿{food['price']}",
                        "type": "text",
                        "weight": "bold",
                        "wrap": True
                    }
                    ],
                    "layout": "baseline",
                    "type": "box"
                }
                ],
                "layout": "vertical",
                "spacing": "sm",
                "type": "box"
            },
            "footer": {
                "contents": [
                {
                    "action": {
                    "label": "Add to Cart",
                    "text": food["food_name"],
                    "type": "message"
                    },
                    "color": "#4fc3f7",
                    "style": "primary",
                    "type": "button"
                }
                ],
                "layout": "vertical",
                "spacing": "sm",
                "type": "box"
            },
            "hero": {
                "aspectMode": "cover",
                "aspectRatio": "20:13",
                "size": "full",
                "type": "image",
                "url": food["img_url"]
            },
            "size": "kilo",
            "type": "bubble"
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