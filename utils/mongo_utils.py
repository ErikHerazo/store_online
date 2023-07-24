from pymongo import MongoClient
import json

class MongoCRUD:
    
    def __init__(self, database_name, collection_name):
        self.database_name = database_name
        self.collection_name = collection_name

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

    def insert_a_SingleDocument(self, data:dict):
        objectInfo = self.collection.insert_one(data)
        message = {
            "message": f'document {objectInfo} was inserted successfully'
        }
        response = json.dumps(message)
        print(response)
        return response

    def insertMultipleDocuments(self, data:list):        
        objectInfo = self.collection.insert_many(data)
        message = {
            "message": f'documents {objectInfo} was inserted successfully'
        }
        response = json.dumps(message)
        print(response)
        return response