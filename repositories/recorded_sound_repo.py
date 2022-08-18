import pymongo
from controller.point import calculate_obtained_point
from models.sound_model import RecordedSound, RecordedSoundRequestBody
from schemas.sounds_schema import recorded_sounds_serializer
from dbconnector import MongoConnector
import datetime

# เชื่อมต่อกับ blind app database
blind_app_db = MongoConnector.connect()
recorded_sounds_col = blind_app_db['recorded_sounds'] # เลือก recorded_sounds collection

def create_recorded_sound(recorded_sound_request_body: RecordedSoundRequestBody):
    new_recorded_sound = dict(recorded_sound_request_body)
    
    result = calculate_obtained_point(
            new_recorded_sound["recorded_url"], 
            new_recorded_sound["played_sound_id"]
        )
    if isinstance(result, int):
        new_recorded_sound["obtained_point"] = result
    else:
        return result # query played_sound error

    new_recorded_sound["timestamp"] = str(datetime.datetime.now())
     
    try:
        _id = recorded_sounds_col.insert_one(new_recorded_sound)
        return {201: recorded_sounds_serializer(recorded_sounds_col.find({"_id": _id.inserted_id}))[0]}
    except pymongo.errors.ConnectionFailure:
        return {520: "Fail to connnect Database"}