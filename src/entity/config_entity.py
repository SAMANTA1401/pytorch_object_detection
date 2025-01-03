from dataclasses import dataclass
from from_root import from_root
from src.constants import *
from src.configuration.s3_operation import S3Operation
import os


@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.S3_OPERATION = S3Operation(),
        self.BUCKET_NAME: str = BUCKET_NAME
        self.ZIP_FILE_NAME:str = ZIP_FILE_NAME
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(from_root(), ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR)
        self.TRAIN_DATA_ARTIFACT_DIR = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_TRAIN_DIR)
        self.TEST_DATA_ARTIFACT_DIR = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_TEST_DIR)
        self.VALID_DATA_ARTIFACT_DIR = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_VALID_DIR)
        self.ZIP_FILE_DIR = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)
        self.ZIP_FILE_PATH = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, self.ZIP_FILE_NAME)
        self.UNZIPPED_FILE_PATH = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, RAW_FILE_NAME)



@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.ROOT_DIR: str = os.path.join(from_root(), ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR)
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(from_root(),ARTIFACTS_DIR,DATA_TRANSFORMATION_ARTIFACTS_DIR)
        self.TRAIN_TRANSFORM_DATA_ARTIFACT_DIR = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR,DATA_TRANSFORMATION_TRAIN_DIR)
        self.TEST_TRANSFORM_DATA_ARTIFACT_DIR = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR,DATA_TRANSFORMATION_TEST_DIR)
        self.TRAIN_TRANSFORM_OBJECT_FILE_PATH = os.path.join(self.TRAIN_TRANSFORM_DATA_ARTIFACT_DIR,
                                                                DATA_TRANSFORMATION_TRAIN_FILE_NAME)
        self.TEST_TRANSFORM_OBJECT_FILE_PATH = os.path.join(self.TEST_TRANSFORM_DATA_ARTIFACT_DIR,
                                                                DATA_TRANSFORMATION_TEST_FILE_NAME)
        
        self.TRAIN_SPLIT = DATA_TRANSFORMATION_TRAIN_SPLIT
        self.TEST_SPLIT = DATA_TRANSFORMATION_TEST_SPLIT



@dataclass
class ModelTrainerConfig:
     def __init__(self):
        self.TRAINED_MODEL_DIR: str = os.path.join(from_root(), ARTIFACTS_DIR, TRAINED_MODEL_DIR)
        self.TRAINED_MODEL_PATH = os.path.join(self.TRAINED_MODEL_DIR, TRAINED_MODEL_NAME)
        self.BATCH_SIZE: int = TRAINED_BATCH_SIZE
        self.SHUFFLE: bool = TRAINED_SHUFFLE
        self.NUM_WORKERS = TRAINED_NUM_WORKERS
        self.EPOCH: int = EPOCH
        self.DEVICE = DEVICE 


@dataclass
class ModelEvaluationConfig:
    def __init__(self):
        self.EVALUATED_MODEL_DIR: str = os.path.join(from_root(), ARTIFACTS_DIR, MODEL_EVALUATION_ARTIFACTS_DIR)
        self.EVALUATED_LOSS_CSV_PATH = os.path.join(self.EVALUATED_MODEL_DIR, MODEL_EVALUATION_FILE_NAME)
        self.BEST_MODEL_PATH = os.path.join(self.EVALUATED_MODEL_DIR, TRAINED_MODEL_NAME )
        self.DEVICE = DEVICE
        self.BATCH: int = 1
        self.SHUFFLE: bool = TRAINED_SHUFFLE
        self.NUM_WORKERS = TRAINED_NUM_WORKERS



@dataclass
class ModelPusherConfig:
    def __init__(self):
        self.TRAINED_MODEL_DIR: str = os.path.join(from_root(),ARTIFACTS_DIR,TRAINED_MODEL_DIR)
        self.BEST_MODEL_PATH: str = os.path.join(self.TRAINED_MODEL_DIR,TRAINED_MODEL_NAME)
        self.BUCKET_NAME: str = BUCKET_NAME
        self.S3_MODEL_KEY_PATH: str = os.path.join(TRAINED_MODEL_NAME)



# a data class is a type of class that mainly contains data and requires little to no boilerplate code. Data classes were introduced in Python 3.7 as a part of PEP 557.
# Benefits of Data Classes
# Data classes provide several benefits, including:
# Less Boilerplate Code: Data classes automatically generate special methods like __init__, __repr__, and __eq__, which reduces the amount of boilerplate code you need to write.

# @dataclass
# class Person:
#     name: str
#     age: int
#     def greet(self):
#         print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# he Person data class has two attributes: name and age. The @dataclass decorator automatically generates the special methods for the class.
# person1 = Person("John Doe", 30)
# person2 = Person("John Doe", 30)

# print(person1)  # Output: Person(name='John Doe', age=30)
# print(person1 == person2)  # Output: True
# person = Person("John Doe", 30)
# person.greet()  # Output: Hello, my name is John Doe and I'm 30 years old.


# from dataclasses import dataclass, field

# @dataclass
# class Person:
#     age: int = field(init=False)
#     name: str

#     def __post_init__(self):
#         self.age = 30

# person = Person("John Doe")
# print(person)  # Output: Person(age=30, name='John Doe')