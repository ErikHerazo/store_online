import json
# import secrets
from pymongo import MongoClient

class MongoCRUD:
    
    def __init__(self, database_name, collection_name):
        self.database_name = database_name
        self.collection_name = collection_name

        # # secret key for mongo session
        # self.tokens_session = secrets.token_hex(20)

        # connection string
        self.uri = f"mongodb+srv://erik1288:ingeniero010@cluster-online-store.ldb3l7j.mongodb.net/{self.database_name}?retryWrites=true&w=majority"
        
        # Create a new client and connect to the server
        self.client = MongoClient(self.uri)
        self.collection = self.client[database_name][self.collection_name]

        # Send a pi ng to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("************** Pinged your deployment. You successfully connected to MongoDB! *****************")
        except Exception as e:
            print(e)

    def insertASingleDocument(self, data:dict):
        objectInfo = self.collection.insert_one(data)
        message = {
            "message": f'document {objectInfo} was inserted successfully'
        }
        return message

    def insertMultipleDocuments(self, data:list):        
        objectInfo = self.collection.insert_many(data)
        message = {
            "message": f'documents {objectInfo} was inserted successfully'
        }
        return message

    def searchDocuments(self, data:dict):
        cursor = self.collection.find(data, {})
        return cursor