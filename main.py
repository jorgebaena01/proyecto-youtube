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





