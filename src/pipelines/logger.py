import logging
import os
from datetime import datetime

dir_name=os.path.join(os.getcwd(),"logs")
os.makedirs(dir_name,exist_ok=True)
file_path=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
log_file_path=os.path.join(dir_name,file_path)

logging.basicConfig(filename=log_file_path,format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging setup is Completed")
