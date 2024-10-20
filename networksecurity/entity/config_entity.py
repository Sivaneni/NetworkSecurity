from datetime import datetime 
import os
from networksecurity.constant import training_pipeline


print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)
class TrainingPipelineConfig:

    '''
    This code defines an initializer method for a class. It sets a default timestamp to the current date and time, formats it as a string ("mm_dd_yyyy_hh_mm_ss"), and assigns it to timestamp. It then initializes three instance variables: pipeline_name and artifact_name from the training_pipeline module, and artifact_dir by joining artifact_name with the formatted timestamp.
    '''
    
    def __init__(self,timestamp=datetime.now()):
        
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifact_name=training_pipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)
        self.time: str=timestamp

        

class DataIngestionConfig:

    '''
    artifact_dir/
    └── data_ingestion_dir/
        ├── feature_store_file_path
        ├── ingested_dir/
        │   ├── training_file_path
        │   └── testing_file_path

    
    '''
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(
                training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME
            )
        self.feature_store_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
            )
        self.training_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
            )
        self.testing_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
            )
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME

        
class DataValidationConfig:
    def __init__(self):
        pass
        

class DataTransformationConfig:
    def __init__(self):
        pass

class ModelTrainerConfig:
    def __init__(self):
        pass

class ModelEvaluationConfig:
    def __init__(self):
        pass

class ModelPusherConfig:
    def __init__(self):
        pass
