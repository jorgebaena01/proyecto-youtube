
#date_format = "%Y-%m-%d"
import pandas as pd
import os
import sys
from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split



import numpy as np

class lipieza_de_datos:
    def __init__(self, nombre_csv):
        self.nombre_csv = nombre_csv
    def limpiador(self):
        try:
            logging.info('corriendo la limpieza')
            df=pd.read_csv(str(self.nombre_csv))
            cambios= {'BARRANQUILLA':'ATLANTICO','STA MARTA D.E.':'MAGDALENA','CARTAGENA':'BOLIVAR'}
            df['departamento_nom']=df['departamento_nom'].replace(cambios)

            df.drop('departamento',axis=1, inplace=True)
            df.drop('ciudad_municipio',axis=1, inplace=True)
            df.drop('ciudad_municipio_nom',axis=1, inplace=True)

            df['fecha_reporte_web']=pd.to_datetime(df['fecha_reporte_web'])
            return df.to_csv("data/clean/datos_limpios.csv")
        except Exception as e:
        
            logging.info('error al limpiar')
            raise CustomException(e,sys)


class splitter:
    def __init__(self, nombre_csv):
        self.nombre_csv = nombre_csv

    def grouper(self):
        try:
            logging.info('agrupando los datos ')
            df=pd.read_csv(str(self.nombre_csv))
            
        
            X=df
            y=df['estado']
            X.drop('estado',axis=1, inplace=True)
    
            X_train, X_test,y_train , y_test = train_test_split(
            X, y, test_size=0.20, random_state=42
            )
            X_train_csv=X_train.to_csv("data/clean/X_train_csv.csv")
            X_test_csv=X_test.to_csv("data/clean/X_test_csv.csv")
            y_train_csv=y_train.to_csv("data/clean/y_train_csv.csv")
            y_test_csv=y_test.to_csv("data/clean/y_test_csv.csv")

            return X_train_csv, X_test_csv, y_train_csv, y_test_csv   # CSV DE ENTRENAMIENTO Y CSV DE PRUEBA
        except Exception as e:
        
            logging.info('error al separar')
            raise CustomException(e,sys)

  

