import logging
import os
from datetime import datetime



def loggeador(x):

    LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    logs_path=os.path.join(os.getcwd(),"logs")
    os.makedirs(logs_path,exist_ok=True)

    LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    return logging.info(x)


from exception import error_message_detail , CustomException
import sys
from logger import logging
#loggeador('corriengo logger papapapa')


if __name__=="__main__":
    try:
        a=1/0

    except Exception as e:
        
        logging.info('empezo el logging')

        raise CustomException(e,sys)


