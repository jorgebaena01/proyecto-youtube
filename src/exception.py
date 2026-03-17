import sys
import logging
#from src.logger import logging
# sys res un modulo con muchas funciones



def error_message_detail(error,error_detail:sys):
    # se llama al modulo .exc_info()   ----> este es para 
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error ocurred in python script named: [{0}], in line numer: [{1}]. The error message is: [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message





class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):

        # En python los argumentos se pasan de una clase madre a una hija por posicion y no por nombre!!!!!!!!!!!!
        # DIOS MIO, DOS HORAS PARA ENTENDER ESOOOOOO
        super().__init__(error_message) # en la clase Exception NO se llama error_message, peeeeero nos importa la posicion, no el nombre de la variable jajajaaja
        self.error_message=error_message_detail(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message
    
from probando_logs import loggeador
if __name__=="__main__":
    try:
        a=1/0

    except Exception as e:
        
        loggeador('loggeando gonorrea')

        raise CustomException(e,sys)

        

