import os
import sys
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging as lg
from src.utils import read_mongo

from sklearn.preprocessing import LabelEncoder

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")

    train_data_path: str = os.path.join("artifacts", "train.csv")

    test_data_path: str = os.path.join("artifacts", "test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    def initiate_data_ingestion(self):
        lg.info('Initiating data ingestion')
        try:
            lg.info('Downloading data from MongoDB Cloud')
            raw = pd.DataFrame(read_mongo())
            lg.info('Dowloading successful')
            lg.info('Data ingestion completed')
            lg.info('Feature Engineering')
            raw.drop(['_id'], axis=1, inplace=True)
            encoder = LabelEncoder()
            raw['Good/Bad'] = encoder.fit_transform(raw['Good/Bad'])

            lg.info("Splitting data into train and test")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            raw.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            train_set, test_set = train_test_split(raw, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            lg.info(f"Ingested data from mongodb to {self.ingestion_config.raw_data_path}")

            lg.info("Exited initiate_data_ingestion method of DataIngestion class")

            return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e, sys)