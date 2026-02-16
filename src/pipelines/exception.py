import os
import sys

def error_detail_message(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno
    error_message=f"Error Occured in filename: {file_name} ,line number : {line_number} :Error {error} "

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        detailed_message=error_detail_message(error_message,error_detail)
        super().__init__(detailed_message)
        self.error_message=detailed_message
        

    def __str__(self):
        return self.error_message
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        raise CustomException(e,sys)

