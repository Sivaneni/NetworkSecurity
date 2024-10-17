import os
import sys
import json

# this below line is used for .env file
from dotenv import load_dotenv
load_dotenv(".env")
MONGO_URI = os.getenv("MONGO_DB_URL")
print(MONGO_URI)
import certifi

ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException   

from networksecurity.logger.logger import logging

# The __init__ method in Python is a special method called a constructor. It’s automatically invoked when a new instance of a class is created. The primary purpose of __init__  is to initialize the object’s attributes and set up any necessary initial state.

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_tojson_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def pushing_data_to_mongodb(self,records,Database,collection):  
        try:
            self.database=Database
            self.collection=collection
            self.records=records

            self.mongoclient=pymongo.MongoClient(MONGO_URI)
            self.database=self.mongoclient[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)

            return len(self.records)
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__ == "__main__":
    file_path="./Network_Data/NetworkData.csv"
    Database="NetworkDatabase"
    collection="NetworkData"

    networkobj=NetworkDataExtract()
    records=networkobj.csv_tojson_convertor(file_path)
    noofrecords=networkobj.pushing_data_to_mongodb(records,Database,collection)
    print(noofrecords)
    #print(records)
        
