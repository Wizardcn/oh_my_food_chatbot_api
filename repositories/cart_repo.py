from dbconnector import *
from schemas import *
from models import *
import pymongo

dse6g1customer_db = MongoConnector.connect()
carts_col = dse6g1customer_db["carts"]

def query_cart(customer_id: str):
    try:
        carts = carts_serializer(carts_col.find({"customer_id": customer_id}))
        # print(carts)
        if len(carts) == 0:
            return {404: "Cart with the customer_id is not available"}
        else:
            return {200: carts[0]}
    except pymongo.errors.ConnectionFailure:
        return {520: "Fail to connect Database"}    


def update_cart(customer_id: str, cart: Cart):
    try:
        result = cart_serializer(carts_col.find_one_and_update({"customer_id": customer_id}, {
            "$set": dict(cart)
        }))
        if result == None:
            return {404: "Fail to update document"}
        else:
            return query_cart(customer_id)

    except pymongo.errors.ConnectionFailure:
        return {520: "Fail to connect database"}