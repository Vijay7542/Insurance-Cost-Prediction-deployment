import os
import sys
import pandas as pd
from src.pipelines import logger
from src.pipelines.exception import CustomException
import logging
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder
from dataclasses import dataclass
from src.pipelines.utils import save_object
from src.componets.data_ingestion import DataIngestion
from src.componets.data_transformation import DataTransformation
from sklearn.ensemble import GradientBoostingRegressor
from src.pipelines.utils import save_object,evalution_metrics

@dataclass
class ModelTrainerConfig:
    model_train_path:str=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.modeltrainerconfig=ModelTrainerConfig()
    def model_train(self):
        try:
            
            logging.info("Model training has been initiated")
            model=GradientBoostingRegressor(random_state=42)#Notebook file we tried multiple models and out of all Gradient Boosting giving good result

            dt_obj=DataTransformation()
            train_arr,test_arr,_=dt_obj.initiate_data_transformation()

            X_train=train_arr[:,:-1]
            y_train=train_arr[:,-1]
            X_test=test_arr[:,:-1]
            y_test=test_arr[:,-1]

            logging.info("input and Outputs features are get seperated")

            model.fit(X_train,y_train)

            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)

            train_metrics=evalution_metrics(y_train,y_train_pred)
            test_metrics=evalution_metrics(y_test,y_test_pred)

            save_object(file_path=self.modeltrainerconfig.model_train_path,obj=model)

            logging.info("file has been saved")

            return (train_metrics,test_metrics)
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    ml_obj=ModelTrainer()
    train_metrics,test_metrics=ml_obj.model_train()
    print("Train Metrics:", train_metrics)
    print("Test Metrics:", test_metrics)




            

