import json
import requests
import settings as ENV

class Mongoatlas():
    mongokey = ENV.MONGO_KEY
    database = ENV.DATABASE_NAME
    datasource = ENV.DATASOURCE
    dataendpoint = ENV.DATA_ENDPOINT

    def __init__(self, collection):
        self.collection = collection

    def insertone(self,document):
        url = "https://data.mongodb-api.com/app/%s/endpoint/data/v1/action/insertOne"%self.dataendpoint
        payload = json.dumps({
            "collection": self.collection,
            "database": Mongoatlas.database,
            "dataSource": Mongoatlas.datasource,
            "document": document
        })
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': Mongoatlas.mongokey 
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()

    def insertmany(self,documentList):
        url = "https://data.mongodb-api.com/app/%s/endpoint/data/v1/action/insertMany"%self.dataendpoint
        payload = json.dumps({
            "collection": self.collection,
            "database": Mongoatlas.database,
            "dataSource": Mongoatlas.datasource,
            "documents": documentList
        })
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': Mongoatlas.mongokey 
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()

    def findone(self,query):
        url = "https://data.mongodb-api.com/app/%s/endpoint/data/v1/action/findOne"%self.dataendpoint
        payload = json.dumps({
            "collection": self.collection,
            "database": Mongoatlas.database,
            "dataSource": Mongoatlas.datasource,
            "filter": query
        })
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': Mongoatlas.mongokey 
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()

    def find(self,query):
        url = "https://data.mongodb-api.com/app/%s/endpoint/data/v1/action/find"%self.dataendpoint
        payload = json.dumps({
            "collection": self.collection,
            "database": Mongoatlas.database,
            "dataSource": Mongoatlas.datasource,
            "filter": query
        })
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': Mongoatlas.mongokey 
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()