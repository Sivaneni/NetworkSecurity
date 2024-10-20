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
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv(".env")

MONGO_URI = os.getenv("MONGO_DB_URL")
print(MONGO_URI)


class DataIngestion:
    '''
    This below code defines an initializer method for a class. It takes a DataIngestionConfig object as a parameter and assigns it to the instance variable self.data_ingestion_config. If an exception occurs during this assignment, it catches the exception and raises a custom NetworkSecurityException, passing the original exception and the sys module for additional context.
    '''
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def export_collection_as_dataframe(self):
        try:
            database_name=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name

            self.mongo_client=pymongo.MongoClient(MONGO_URI)
            collection=self.mongo_client[database_name][collection_name]
            '''
            The below  code snippet converts MongoDB query results into a pandas DataFrame. It checks if the “_id” column exists and removes it. Then, it replaces any occurrences of the string “na” with NaN values and returns the cleaned DataFrame.'''
            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df=df.drop("_id",axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df

        except Exception as e:
            raise NetworkSecurityException(e, sys)
    # Feast is a standalone, open-source feature store that organizations use to store and serve features consistently for offline training and online inference. 
    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe

        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        try:
            train_set,test_set=train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio)

            dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Exporting train and test file path.")
            train_set.to_csv(
                self.data_ingestion_config.training_file_path,index=False,header=True
                )
            test_set.to_csv(
                self.data_ingestion_config.testing_file_path,index=False,header=True
            )
            logging.info(f"Exported train and test file path.")
             
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def initiate_data_ingestion(self):
        try:
            dataframe=self.export_collection_as_dataframe()
            dataframe=self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe=dataframe)
            data_ingestion_artifact=DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,test_file_path=self.data_ingestion_config.testing_file_path)

            return data_ingestion_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)

