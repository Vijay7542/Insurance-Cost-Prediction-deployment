import os
import sys
import pandas as pd
from src.pipelines import logger
from src.pipelines.exception import CustomException
import logging
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_file_path:str=os.path.join("artifacts","train.csv")
    test_file_path:str=os.path.join("artifacts","test.csv")
    raw_file_path:str=os.path.join("artifacts","raw.csv")


class DataIngestion:
    def __init__(self):
        self.dataingestionconfig=DataIngestionConfig()
        logging.info("Initiate Data Ingestion")
        
    def initiate_data_ingestion(self):
        os.makedirs("artifacts",exist_ok=True)
        try:
            df=pd.read_csv(r"notebook\data\insurance.csv")

            df.to_csv(self.dataingestionconfig.raw_file_path,index=False)

            logging.info("Insurance data file is stored in artifact folder")

            train_set,test_set=train_test_split(df,test_size=0.20,random_state=42)

            train_set.to_csv(self.dataingestionconfig.train_file_path,index=False)
            test_set.to_csv(self.dataingestionconfig.test_file_path,index=False)

            logging.info("Both train and test set has been stored in the artifact folder")
            return (self.dataingestionconfig.train_file_path,self.dataingestionconfig.test_file_path)
        
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_path,test_path=obj.initiate_data_ingestion()
            

    

