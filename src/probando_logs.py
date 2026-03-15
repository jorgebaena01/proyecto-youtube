import logging
from src.logger import logging
import sys
logging.info("Ocurrió un error")
try:
    a = 1/0
except Exception as e:
    logging.info("Ocurrió un error")
    raise CustomException(e, sys)




logging.info("Ocurrió un error")