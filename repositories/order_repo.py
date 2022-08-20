from dbconnector import *
from schemas import *
from models import *
import pymongo

dse6g1customer_db = MongoConnector.connect()
orders_col = dse6g1customer_db["orders"]

def query_order(customer_id: str):
    try:
        orders = orders_serializer(orders_col.find({"customer_id": customer_id}))
        if len(orders) == 0:
            return {404: "Order with the customer_id is not available"}
        else:
            return {200: orders[0]}
    except pymongo.errors.ConnectionFailure:
        return {520: "Fail to connect Database"}    
    
    
def create_order(customer_id: str, display_name: str, timestamp: str, cart: list):
    
    try:
        _id = orders_col.insert_one({
            "customer_id": customer_id,
            "display_name": display_name,
            "timestamp": timestamp,
            "cart": cart
        })
        return {201: orders_serializer(orders_col.find({"_id": _id.inserted_id}))[0]}
    except pymongo.errors.ConnectionFailure:
        return {520: "Fail to connect Database"}
