from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from services import food_router
from services import cart_router



app = FastAPI()

# # อันนี้เดี๋ยวใส่ Domain ที่อนุญาตให้เข้าถึง API แต่ตอนนี้ขออนุญาตทุก Domain ไปก่อน
# origins = [
#     "http://localhost:8080",
#     "http://localhost:3000",
# ]

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/", tags=["root"], response_class=HTMLResponse)
def serve_home(request: Request):
    return templates.TemplateResponse("/home.html",{"request":request})

app.include_router(food_router, prefix='/service/foods')
app.include_router(cart_router, prefix="/service/carts")