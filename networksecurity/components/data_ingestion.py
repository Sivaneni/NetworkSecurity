from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

#configuration of component and artifact generation

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

import os
import sys
import pandas as pd
import numpy as np
import pymongo
from typing import List
from dotenv import load_dotenv
load_dotenv(".env")

MONGO_URI = os.getenv("MONGO_DB_URL")
print(MONGO_URI)


class DataIngestion:

    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def export_collection_as_dataframe(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    # Feast is a standalone, open-source feature store that organizations use to store and serve features consistently for offline training and online inference. 
    def export_data_into_feature_store(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def split_data_as_train_test(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

