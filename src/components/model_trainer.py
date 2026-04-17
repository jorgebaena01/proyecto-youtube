
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import datetime as dt
import pandas as pd
from src.exception import CustomException
from src.logger import logging
import sys
#MODELOS QUE PIENSO USAR:
    #LINEAR REGRESSION

    


class ModelTrainer:
    def __init__(self,xtest,xtrain,ytest,ytrain):
        self.xtest=xtest
        self.xtrain=xtrain
        self.ytest=ytest
        self.ytrain=ytrain

    def linear_regression(self):
        try:
            xtest_=pd.read_csv(str(self.xtest))
            xtest_['fecha_reporte_web']=pd.to_datetime(xtest_['fecha_reporte_web'])
            xtest_['fecha_reporte_web']=xtest_['fecha_reporte_web'].map(dt.datetime.toordinal)
            xtest_=xtest_[['fecha_reporte_web']]        



            xtrain_=pd.read_csv(str(self.xtrain))
            xtrain_['fecha_reporte_web']=pd.to_datetime(xtrain_['fecha_reporte_web'])
            xtrain_['fecha_reporte_web']=xtrain_['fecha_reporte_web'].map(dt.datetime.toordinal)
            xtrain_=xtrain_[['fecha_reporte_web']]

            ytrain_ = pd.read_csv(str(self.ytrain))

    #  LIMPIEZA PRIMERO
            xtrain_ = xtrain_.dropna()
            ytrain_ = ytrain_.loc[xtrain_.index]
    
            ytrain_ = ytrain_.dropna()
            xtrain_ = xtrain_.loc[ytrain_.index]
    
    #  CONVERTIR DESPUÉS
            le = LabelEncoder()
            ytrain_ = ytrain_.iloc[:, 0]
            ytrain_ = le.fit_transform(ytrain_)
    
            xtest_ = xtest_.dropna()
    
            model = LinearRegression()
            model.fit(xtrain_, ytrain_)
            
            y_pred = model.predict(xtest_)
            return print(y_pred)
            
            #print("YA FUNCIONÓ , ypred es:",y_pred)
        except Exception as e:
            logging.info('error al separar')
            raise CustomException(e,sys)
        
            



ModelTrainer('data/clean/X_test_csv.csv','data/clean/X_train_csv.csv',2,'data/clean/y_train_csv.csv').linear_regression()