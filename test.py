
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://sivaneniprasanna4:kwkkdxk9Sjsi4l8T@cluster0.b5cqe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)