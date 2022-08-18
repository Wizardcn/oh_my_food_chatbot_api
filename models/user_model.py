from pydantic import BaseModel


class CreateUserRequestBody(BaseModel):
    uid: str
    username: str
    email: str
    password: str
    profile_pic_url: str
    
    class Config:
        schema_extra = {
            "example": {
                "uid": '213421414213412',
                "username": "superman123",
                "email": "superman123@gmail.com",
                "password": "admin1234",
                "profile_pic_url": "https://cdn.discordapp.com/attachments/983275821630357534/994459026320543764/userimg2.jpg"
            }
        }

class User(BaseModel):
    uid: str
    username: str
    email: str
    password: str
    total_point: int
    profile_pic_url: str = "https://cdn.discordapp.com/attachments/983275821630357534/994459026320543764/userimg2.jpg"
    record_history: dict
    
    class Config:
        schema_extra = {
            "example": {
                "uid": '213421414213412',
                "username": "superman123",
                "email": "superman123@gmail.com",
                "password": "Superman@354651",
                "total_point": 10,
                "profile_pic_url": "https://cdn.discordapp.com/attachments/983275821630357534/994459026320543764/userimg2.jpg",
                "record_history": {
                    "62d10bc963a10aff11ad3cf5": "T00001",
                    "62d10c5b0f6b2df15b608315": "T00001",
                    "62d10c910f6b2df15b608316": "T00002"
                }
            },
        }
    
    
class ShowUser(BaseModel):
    uid: str
    username: str
    email: str
    total_point: int
    profile_pic_url: str = "https://cdn.discordapp.com/attachments/983275821630357534/994459026320543764/userimg2.jpg"
    record_history: dict
    
    
    class Config:
        schema_extra = {
            "example": {
                "uid": '213421414213412',
                "username": "superman123",
                "email": "superman123@gmail.com",
                "total_point": 0,
                "profile_pic_url": "https://cdn.discordapp.com/attachments/983275821630357534/994459026320543764/userimg2.jpg",
                "hist_record": {}
            },
        }
    