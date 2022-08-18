from pydantic import BaseModel


class PlayedSound(BaseModel):
    played_sound_id: str 
    played_sound_url: str
    count: int
    max_point: int # max point that user will obtain
    
    class Config:
        schema_extra = {
            "example": {
                "played_sound_id": "T00001",
                "played_sound_url": "https://drive.google.com/uc?export=download&id=141pWgdaUA8-yHH1ZAxOv-xXrlGBJ6OIr",
                "count": 0,
                "max_point": 10
                }
        }
        
        
class RecordedSound(BaseModel):
    recorded_id: str # auto gen mongodb
    played_sound_id: str # from PlayedSound class
    recorded_url: str # url ที่ได้มากจากการฝากไฟล์เสียงใน cloud storage
    obtained_point: int # point ที่ได้รับ (มี algorithm ในการคำนวณแต่ยังคิดไม่ออก)
    uid: str # uid ของคนที่อัดเสียง
    timestamp: str # generate by our API in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm)
    
    class Config:
        schema_extra = {
            "example": {
                "recorded_id": "62afdaaf58723fcfca45e8d1",
                "played_sound_id": "T00001",
                "recorded_url": "https://drive.google.com/uc?export=download&id=141pWgdaUA8-yHH1ZAxOv-xXrlGBJr",
                "obtained_point": "10",
                "uid": "129dfjk210dsfk",
                "timestamp": "2022-07-15 12:49:31.655309"
            }
        }
        
        
class RecordedSoundRequestBody(BaseModel):
    # recorded_id: str # auto gen mongodb
    played_sound_id: str # from PlayedSound class
    recorded_url: str # url ที่ได้มากจากการฝากไฟล์เสียงใน cloud storage
    # obtained_point: int # point ที่ได้รับ (มี algorithm ในการคำนวณแต่ยังคิดไม่ออก)
    uid: str # uid ของคนที่อัดเสียง
    # timestamp: str # generate by our API in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm)
    
    class Config:
        schema_extra = {
            "example": {
                "played_sound_id": "T00001",
                "recorded_url": "https://drive.google.com/uc?export=download&id=141pWgdaUA8-yHH1ZAxOv-xXrlGBJr",
                "uid": "129dfjk210dsfk"
            }
        }
        
        
class ShowPlayedSounds(BaseModel):
    
    class Config:
        schema_extra = {
            "example": [
                {
                    "played_sound_id": "T00001",
                    "played_sound_url": "https://drive.google.com/uc?export=download&id=141pWgdaUA8-yHH1ZAxOv-xXrlGBJ6OIr",
                    "count": 0,
                    "max_point": 10
                },
                {
                    "played_sound_id": "T00002",
                    "played_sound_url": "https://drive.google.com/uc?export=download&id=141pWgdaUA8-yHH1ZAxOv-xXrlGBJ6OIr",
                    "count": 0,
                    "max_point": 10
                }
            ]
        }