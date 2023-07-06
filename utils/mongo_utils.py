from pymongo import MongoClient

uri = "mongodb+srv://erik1288:ingeniero010@cluster0.8sltkuy.mongodb.net/cluster0?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client['cluster0']
print(db)

# Send a pi ng to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)