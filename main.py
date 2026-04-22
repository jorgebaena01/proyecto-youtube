'''
LA IDEA DE ESTE CODIGO MAIN ES CORRER TODO JUNTO!!!




'''

import pandas as pd
import random
import sys
from sodapy import Socrata
from src.components.claves import username_jorge, password_jorge
from src.exception import error_message_detail, CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import datetime as dt
import os


from src.components.data_ingestion import ingesta
ingesta()


from src.components.data_transformation import lipieza_de_datos
from src.components.data_transformation import splitter

x=lipieza_de_datos('data/raw/datos_crudos.csv')
x.limpiador()

y=splitter('data/clean/datos_limpios.csv')
y.grouper()



from src.components.model_trainer import ModelTrainer

z=ModelTrainer('data/clean/X_test_csv.csv','data/clean/X_train_csv.csv',2,'data/clean/y_train_csv.csv')
z.linear_regression()
