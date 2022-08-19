from lib2to3.pytree import Base
from pydantic import BaseModel

class Cart(BaseModel):
    customer_id: str
    cart: list

    class Config:
        schema_extra = {
            "example": {
                "customer_id": "U45029b0ec683201a3b77414534d3d7a9",
                "cart": [
                            {"food_id": "food00001", "amount": 5},
                            {"food_id": "food00003", "amount": 4}
                ]
            }
        }
        
        
class CartFlex(BaseModel):
    
    class Config:
        schema_extra = {
            "example": {
                "response_type": "object",
                "line_payload": {
                    "type": "flex",
                    "altText": "this is a flex message",
                    "contents": {
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
                                "text": "ตะกร้าสินค้า: 35 ชิ้น",
                                "type": "text",
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "borderWidth": "none",
                                "contents": [
                                {
                                    "aspectMode": "fit",
                                    "flex": 1,
                                    "margin": "none",
                                    "size": "full",
                                    "type": "image",
                                    "url": "https://www.chillpainai.com/src/wewakeup/scoop/img_scoop/scoop/somm/ttk1.jpg"
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
                                        "text": "ปลาดิบ",
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
                                        "text": "x5",
                                        "type": "text"
                                    },
                                    {
                                        "align": "end",
                                        "color": "#757c88",
                                        "text": "฿200",
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
                            },
                            {
                                "borderWidth": "none",
                                "contents": [
                                {
                                    "aspectMode": "fit",
                                    "flex": 1,
                                    "margin": "none",
                                    "size": "full",
                                    "type": "image",
                                    "url": "https://img.wongnai.com/p/1920x0/2017/06/08/25c3c81cddc14e6ca520e0681fb518b6.jpg"
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
                                        "text": "ก๋วยเตี๋๋ยวต้มยำไข่",
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
                                        "text": "x10",
                                        "type": "text"
                                    },
                                    {
                                        "align": "end",
                                        "color": "#757c88",
                                        "text": "฿50",
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
                            },
                            {
                                "borderWidth": "none",
                                "contents": [
                                {
                                    "aspectMode": "fit",
                                    "flex": 1,
                                    "margin": "none",
                                    "size": "full",
                                    "type": "image",
                                    "url": "https://www.chillpainai.com/src/wewakeup/scoop/img_scoop/scoop/somm/ttk1.jpg"
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
                                        "text": "ปลาดิบ",
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
                                        "text": "x5",
                                        "type": "text"
                                    },
                                    {
                                        "align": "end",
                                        "color": "#757c88",
                                        "text": "฿200",
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
                            },
                            {
                                "borderWidth": "none",
                                "contents": [
                                {
                                    "aspectMode": "fit",
                                    "flex": 1,
                                    "margin": "none",
                                    "size": "full",
                                    "type": "image",
                                    "url": "https://www.chillpainai.com/src/wewakeup/scoop/img_scoop/scoop/somm/ttk1.jpg"
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
                                        "text": "ปลาดิบ",
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
                                        "text": "x5",
                                        "type": "text"
                                    },
                                    {
                                        "align": "end",
                                        "color": "#757c88",
                                        "text": "฿200",
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
                            },
                            {
                                "borderWidth": "none",
                                "contents": [
                                {
                                    "aspectMode": "fit",
                                    "flex": 1,
                                    "margin": "none",
                                    "size": "full",
                                    "type": "image",
                                    "url": "https://www.chillpainai.com/src/wewakeup/scoop/img_scoop/scoop/somm/ttk1.jpg"
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
                                        "text": "ปลาดิบ",
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
                                        "text": "x5",
                                        "type": "text"
                                    },
                                    {
                                        "align": "end",
                                        "color": "#757c88",
                                        "text": "฿200",
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
                            },
                            {
                                "borderWidth": "none",
                                "contents": [
                                {
                                    "aspectMode": "fit",
                                    "flex": 1,
                                    "margin": "none",
                                    "size": "full",
                                    "type": "image",
                                    "url": "https://www.chillpainai.com/src/wewakeup/scoop/img_scoop/scoop/somm/ttk1.jpg"
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
                                        "text": "ปลาดิบ",
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
                                        "text": "x5",
                                        "type": "text"
                                    },
                                    {
                                        "align": "end",
                                        "color": "#757c88",
                                        "text": "฿200",
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
                            ]
                        },
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
                                "text": "฿5500.00",
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
                            "label": "ชำระเงิน",
                            "data": "DL_ชำระเงิน"
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
                }
            }
  
        }

class AddFoodRequestBody(BaseModel):
    customer_id: str
    food_name: str
    amount: int
    
    class Config: 
        schema_extra = {
            "example": {
                "customer_id": "U45029b0ec683201a3b77414534d3d7a9",
                "food_name": "ปลาดิบ",
                "amount": 5
            }
        }