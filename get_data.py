import os
import sys
import json

# this below line is used for .env file
from dotenv import load_dotenv
load_dotenv
MONGO_URI = os.getenv("MONGO_URI")
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
        
    def csv_tojson_convertor(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def pushing_data_to_mongodb(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    if __name__ == "__main__":
        pass
        
