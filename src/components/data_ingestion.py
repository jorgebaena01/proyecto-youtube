


import pandas as pd
import random
import sys
from sodapy import Socrata
from src.components.claves import username_jorge, password_jorge
from src.exception import error_message_detail, CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split




df_vacio=pd.DataFrame(columns=['fecha_reporte_web', 'id_de_caso', 'fecha_de_notificaci_n',
       'departamento', 'departamento_nom', 'ciudad_municipio',
       'ciudad_municipio_nom', 'edad', 'unidad_medida', 'sexo',
       'fuente_tipo_contagio', 'ubicacion', 'estado', 'recuperado',
       'fecha_inicio_sintomas', 'fecha_muerte', 'fecha_diagnostico',
       'per_etn_', 'fecha_recuperado', 'tipo_recuperacion', 'nom_grupo_'])



# Es necesario partir la lista en listas pequenas para llamar los datos varias veces
numeros_unicos = random.sample(range(1, 6391012), 20000)
numeros_str = list(map(str, numeros_unicos))

logging.info("Iniciando el proceso de ingesta de datos desde Socrata...")


def ingesta():
    try:

        df_vacio=pd.DataFrame(columns=['fecha_reporte_web', 'id_de_caso', 'fecha_de_notificaci_n',
       'departamento', 'departamento_nom', 'ciudad_municipio',
       'ciudad_municipio_nom', 'edad', 'unidad_medida', 'sexo',
       'fuente_tipo_contagio', 'ubicacion', 'estado', 'recuperado',
       'fecha_inicio_sintomas', 'fecha_muerte', 'fecha_diagnostico',
       'per_etn_', 'fecha_recuperado', 'tipo_recuperacion', 'nom_grupo_'])

        for i in range(0,20000,500):

            lista=numeros_str[i:i+500]
            lista=tuple(lista)
            #print(lista)

            client = Socrata(
                "www.datos.gov.co",
                None,
                username=username_jorge,
                password=password_jorge
            )


            # ITERANDO SAQUE EL ID MAX, ESTO DEBIDO A QUE NO CONTABA CON LA DOCUMENTACION PARA HACER LAS QUERIES DE LA FORMA APROPIADA
            results = client.get(
                "gt2j-8ykr",
                where=f"id_de_caso in {lista}",
                limit=500
            )


            resultado1=pd.DataFrame.from_records(results)
            df_vacio=pd.concat([df_vacio,resultado1],ignore_index=True)
        df_vacio["id_de_caso"] = pd.to_numeric(df_vacio["id_de_caso"], errors="coerce").fillna(0).astype(int)
        return df_vacio.to_csv("src/components/datos_crudos.csv")
    except Exception as e:
        
        logging.info('salio mal')

        raise CustomException(e,sys)

ingesta()


logging.info("SE TERMINO DE CORRER EL BUCLE")




'''
print('el valor maximo es:',df_vacio['id_de_caso'].max())
print('el valor promedio es:',df_vacio['id_de_caso'].mean())
print('esta vuelta tiene:',len(df_vacio),'filas')
print(df_vacio.head())'''


print('sssssssttttttt')




