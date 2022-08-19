import pymongo
from dbconnector import *
from schemas import *


dse6g1customer_db = MongoConnector.connect()
foods_col = dse6g1customer_db["foods"]

def query_with_food_id(food_id_list: list):
    try:
        foods = foods_serializer(foods_col.find({"food_id": {
            "$in": food_id_list
        }}))
        if len(foods) == 0:
            return {404: "Foods with these food_id is not available"}
        else:
            return {200: foods}
    except pymongo.errors.ConnectionFailure:
        return {520: "Fail to connect Database"}

def query_with_food_name(food_name: str):
    try:
        foods = foods_serializer(foods_col.find({"food_name": food_name}))
        if len(foods) == 0:
            return {404: "Food with the food_name is not available"}
        else:
            return {200: foods[0]}
    except pymongo.errors.ConnectionFailure:
        return {520: "Fail to connect Database"}