from dataclasses import dataclass
import pandas as pd
import os
from src.pipelines.utils import load_pickle_file
import pickle
from src.pipelines import logger
from src.pipelines.exception import CustomException
import sys
import logging


class PredictPipeline:
    def __init__(self):
        pass
    def predict_data(self,dataframe_features):
        try:
            
    
            model_pickle_path=os.path.join("artifacts","model.pkl")
            preprocessor_pickle_path=os.path.join("artifacts","preprocessor.pkl")

            model=load_pickle_file(file_path=model_pickle_path)
            preprocessor=load_pickle_file(file_path=preprocessor_pickle_path)

            logging.info("pickle files have been loaded")

            preprocessed_dataframe=preprocessor.transform(dataframe_features)

            logging.info("data scaling has been completed")

            data_prediction=model.predict(preprocessed_dataframe)

            return data_prediction
        
        except Exception as e:
            raise CustomException(e,sys)
    

        

class UserData:
    def __init__(self,age:int,sex:str,bmi:float,children:int,smoker:str,region:str):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region=region

    def create_data_frame(self):
        data={"age":self.age,"sex":self.sex,"bmi":self.bmi,"children":self.children,"smoker":self.smoker,"region":self.region}
        
        logging.info("Data Frame is created")
        
        return pd.DataFrame([data])
    
    
    
if __name__=="__main__":
    user_obj=UserData(age=23,sex="male",bmi=22.3,children=1,smoker="yes",region="southwest")
    dataframe=user_obj.create_data_frame()
    print(dataframe)
    pred_obj=PredictPipeline()
    result=pred_obj.predict_data(dataframe)
    print(result[0])




    

        