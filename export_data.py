import sys
import pandas as pd
from src.exception import CustomException
from src.utils import write_mongo

try:
    data = pd.read_csv("notebooks/wafers.csv")
    write_mongo(data)    

except Exception as e:
    raise CustomException(e, sys)