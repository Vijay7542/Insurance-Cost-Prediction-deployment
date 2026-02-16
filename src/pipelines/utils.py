import os
import sys
import pickle
from src.pipelines.exception import CustomException
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error

def save_object(file_path,obj):
    try:
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
def evalution_metrics(true,predicted):
    R2_score=r2_score(true,predicted)
    mse=mean_squared_error(true,predicted)
    mae=mean_absolute_error(true,predicted)

    return R2_score,mse,mae

def load_pickle_file(file_path):
    try:
        with open(file_path,"rb") as file:
            obj_pickle_file=pickle.load(file)
        return obj_pickle_file
    except Exception as e:
        raise CustomException(e,sys)
    