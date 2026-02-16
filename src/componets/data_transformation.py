import os
import sys
import pandas as pd
from src.pipelines import logger
from src.pipelines.exception import CustomException
import logging
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.pipelines.utils import save_object
from src.componets.data_ingestion import DataIngestion
import numpy as np

@dataclass
class DataTransformationConfig:

    preprocessor_file_path:str=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):

        self.datatransformationconfig=DataTransformationConfig()

    def data_pipeline(self):
        try:
            os.makedirs("artifacts",exist_ok=True)

            logging.info("data pipeline has been initiated")

            num_columns=["age","bmi","children"]
            cat_columns=["sex","smoker","region"]

            num_pipeline=Pipeline([("imputer",SimpleImputer(strategy="mean")),("scaler",StandardScaler())])
            cat_pipeline=Pipeline([("imputer",SimpleImputer(strategy="most_frequent")),("onehotencoding",OneHotEncoder(handle_unknown="ignore")),("scaler",StandardScaler(with_mean=False))])

            preprocessor=ColumnTransformer([("numerical_pipeline",num_pipeline,num_columns),("categorical_pipeline",cat_pipeline,cat_columns)])

            logging.info("preprocessor pipeline is Created")


            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
    def initiate_data_transformation(self):
        try:
            logging.info("Data trasformation has been initiated")

            ingestion_obj=DataIngestion()

            train_path,test_path=ingestion_obj.initiate_data_ingestion()
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Both Train and test files have been read")

            input_train_df=train_df.drop("charges",axis=1)
            output_feature="charges"
            output_train_df=train_df[output_feature]

            input_test_df=test_df.drop("charges",axis=1)
            output_test_df=test_df[output_feature]

            preprocessor_obj=self.data_pipeline()

            preprocessed_train_df=preprocessor_obj.fit_transform(input_train_df)
            preprocessed_test_df=preprocessor_obj.transform(input_test_df)

            train_arr = np.c_[preprocessed_train_df, np.array(output_train_df)]
            test_arr = np.c_[preprocessed_test_df, np.array(output_test_df)]

            logging.info("train and test array created")

            save_object(file_path=self.datatransformationconfig.preprocessor_file_path,obj=preprocessor_obj)
            logging.info("preprocessor pickle has been saved")


            return (train_arr,test_arr,self.datatransformationconfig.preprocessor_file_path)
        except Exception as e:
            raise CustomException(e,sys)
          
            
if __name__=="__main__":
    obj=DataTransformation()
    train,test,_=obj.initiate_data_transformation()
    logging.info("All good")






