import os
import sys
import dill
import pandas as pd
from py_dotenv import dotenv
from pymongo import MongoClient

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging as lg

def read_mongo():
    try:
            lg.info('Connecting to MongoDB Cloud')
            dotenv.read_dotenv('.env')
            client = os.getenv('client')
            lg.info('Connection successful')
            
            database = os.getenv('database')
            collection = os.getenv('collection')            

            client = MongoClient(client)
            db = client[database]
            collection = db[collection]
            cursor = collection.find({}) 
            data = list(cursor)
            client.close()
            return data
    
    except Exception as e:
        raise CustomException(e, sys)

def write_mongo(data):
    try:
            lg.info('Connecting to MongoDB Cloud')
            dotenv.read_dotenv('.env')
            database = os.getenv('database')
            collection = os.getenv('collection')
            client = MongoClient(os.getenv('client'))
            lg.info('Connection successful')   
            db = client[database]
            collection = db[collection]
            lg.info('Storing data into MongoDB Cloud') 
            data['_id'] = range(1, len(data) + 1)
            data = data.to_dict(orient='records')
            collection.insert_many(data)
            lg.info('Data successfully stored in MongoDB Cloud') 
    except Exception as e:
        raise CustomException(e, sys)


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)



def evaluate_models(X, y, models):
    try:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(X_train, y_train)  # Train model
            y_test_pred = model.predict(X_test)

            test_model_score = accuracy_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
