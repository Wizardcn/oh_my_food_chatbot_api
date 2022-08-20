import pymongo
from dbconnector import *
from schemas import *


dse6g1customer_db = MongoConnector.connect()
knowledges_col = dse6g1customer_db["knowledges"]


def query_knowledges_with_sub_topic(sub_topic: str):

    try:
        knowledges = knowledges_serializer(knowledges_col.find({"sub-topic": sub_topic}))
        if len(knowledges) == 0:
            return {404: "Knowledges with the sub-topic is not available"}
        else:
            return {200: knowledges[0]}
    except pymongo.errors.ConnectionFailure:
        return {520: "Fail to connect Database"}
