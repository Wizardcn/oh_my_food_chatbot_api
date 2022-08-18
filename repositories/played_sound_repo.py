import pymongo
from models import PlayedSound
from schemas.sounds_schema import played_sounds_serializer
from dbconnector import MongoConnector

# เชื่อมต่อกับ blind app database
blind_app_db = MongoConnector.connect()
played_sounds_col = blind_app_db['played_sounds'] # เลือก played_sounds collection

def query_played_sound(played_sound_id: str):
    try:
        played_sounds = played_sounds_serializer(played_sounds_col.find({"played_sound_id": played_sound_id}))
        if len(played_sounds) == 0:
            return {404: "Played sound with the played_sound_id is not available"}
        else:
            return {200: played_sounds[0]}
    except pymongo.errors.ConnectionFailure:
        return {520: "Fail to connnect Database"}
    
    
# def count_played_sounds():
#     try:
#         return {200: played_sounds_col.count_documents({})}
#     except pymongo.errors.ConnectionFailure:
#         return {520: "Fail to connnect Database"}
    
    
def update_played_sound(played_sound_id: str, played_sound: PlayedSound):
    try:
        result = played_sounds_col.find_one_and_update({"played_sound_id": played_sound_id}, {
            "$set": dict(played_sound)
        })
        if result == None:
            return {404: "Played sound with the played_sound_id is no document matches"}
        else:
            return query_played_sound(played_sound_id)
    except pymongo.errors.ConnectionFailure:
        return {520: "Fail to connnect Database"}
    
    
def query_played_sounds():
    try:
        played_sounds = played_sounds_serializer(played_sounds_col.find({}))
        if len(played_sounds) == 0:
            return {404: "Played sound with the played_sound_id is not available"}
        else:
            return {200: played_sounds}
    except pymongo.errors.ConnectionFailure:
        return {520: "Fail to connnect Database"}
        