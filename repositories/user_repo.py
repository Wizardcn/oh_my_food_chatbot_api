import pymongo
from models.user_model import CreateUserRequestBody
from schemas.users_schema import users_serializer
from dbconnector import MongoConnector
from models import User
from utils.hashing import get_password_hash

# เชื่อมต่อกับ blind app database
blind_app_db = MongoConnector.connect()
users_col = blind_app_db['users'] # เลือก users collection

def create_user(user: CreateUserRequestBody):
    new_user = dict(user)
    new_user["password"] = get_password_hash(new_user["password"])
    new_user["total_point"] = 0
    new_user["record_history"] = {}
    
    try: 
        _id = users_col.insert_one(new_user)
        return {201: users_serializer(users_col.find({"_id": _id.inserted_id}))}
    except pymongo.errors.ConnectionFailure:
        return {520: "Fail to connect Database"}


def query_user(uid: str):
    try:
        users = users_serializer(users_col.find({"uid": uid}))
        if len(users) == 0:
            return {404: "User with the uid is not available"}
        else:
            return {200: users[0]}
    except pymongo.errors.ConnectionFailure:
        return {520: "Fail to connect Database"}


def update_user(uid: str, user: User):
    try:
        user = dict(user)
        if "id" in user:
            del user["id"]
        result = users_col.find_one_and_update({"uid": uid}, {
            "$set": dict(user)
        })
        if result == None:
            return {404: "User with the uid is no document matches"}
        else:
            return query_user(uid)
    except pymongo.errors.ConnectionFailure:
        return {520: "Fail to connect Database"}