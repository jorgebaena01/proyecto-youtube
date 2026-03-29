
#date_format = "%Y-%m-%d"
import pandas as pd
import os
import sys
from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split


class lipieza_de_datos:
    pass



class split:
    def __init__(self, nombre_csv):
        self.nombre_csv = nombre_csv

    def grouper(self):
        df=pd.read_csv(str(self.nombre_csv))
        return df
        #Ahora sigue la particion entre datos de entrenamiento y prueba

