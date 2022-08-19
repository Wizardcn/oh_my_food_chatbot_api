import settings as ENV
from utils import Singleton
from pymongo import MongoClient

class MongoConnector(metaclass = Singleton):
    client = MongoClient(ENV.MONGO_URI)
    cl = client[ENV.DATABASE_NAME]

    @classmethod
    def connect(cls) -> MongoClient:
        return cls.cl

    @classmethod
    def disconnect(cls):
        return cls.client.close()