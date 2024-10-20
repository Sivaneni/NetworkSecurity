from dataclasses import dataclass


'''

This code defines a data class named DataIngestionArtifact using the @dataclass decorator. It has two attributes:

trained_file_path: A string representing the path to the trained data file.
test_file_path: A string representing the path to the test data file.
Data classes automatically generate special methods like __init__, __repr__, and __eq__, making it easier to manage and use these attributes.
'''
@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str
@dataclass
class DataValidationArtifact:
    pass
@dataclass
class DataTransformationArtifact:
    pass
@dataclass
class ModelTrainerArtifact:
    pass
@dataclass
class ModelEvaluationArtifact:
    pass
@dataclass
class ModelPusherArtifact:
    pass
@dataclass
class classificationMetricArtifact:
    pass
