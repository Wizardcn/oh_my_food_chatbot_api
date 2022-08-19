from pydantic import BaseModel


class Food(BaseModel):
    food_id: str
    food_name: str
    img_url: str
    price: int

class FoodFlex(BaseModel):
    class Config:
        schema_extra = {
            "example": {
            "response_type": "object",
            "line_payload": [
                {
                "type": "flex",
                "altText": "this is a flex message",
                "contents": {
                    "type": "carousel",
                    "contents": [
                    {
                        "type": "bubble",
                        "size": "kilo",
                        "hero": {
                        "type": "image",
                        "url": "https://1.bp.blogspot.com/--FD2WH6Gscw/XMyPag0LGFI/AAAAAAAAAAQ/do_5M9jddE47hhQlNStYMa2Ni4s6IPsZwCEwYBhgL/s1600/2ce2bec237b68b155f02bb482acfb7dc.jpg",
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
                                "text": "ผัดเผ็ดปลาดุก",
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
                                "text": "฿70"
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
                                "text": "ผัดเผ็ดปลาดุก"
                            }
                            }
                        ]
                        }
                    },
                    {
                        "type": "bubble",
                        "size": "kilo",
                        "hero": {
                        "type": "image",
                        "url": "https://www.chillpainai.com/src/wewakeup/scoop/img_scoop/scoop/somm/ttk1.jpg",
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
                                "text": "ปลาดิบ",
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
                                "text": "฿200"
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
                                "text": "ปลาดิบ"
                            }
                            }
                        ]
                        }
                    }
                    ]
                }
                }
            ]
            }
        }
        
        
class FoodIdRequestBody(BaseModel):
    food_id_list: list
    
    class Config:
        schema_extra = {
            "example": {
                "food_id_list": ["food00001", "food00023"]
            }
        }