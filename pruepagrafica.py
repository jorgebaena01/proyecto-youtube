import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
df = pd.read_csv('data/raw/datos_crudos.csv')
df.head()

df['fecha_reporte_web'].dtype
df['fecha_reporte_web']=pd.to_datetime(df['fecha_reporte_web'])
print(df['fecha_reporte_web'].dtype)
df1=df["fecha_reporte_web"].value_counts().sort_index()


plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'white'

plt.style.use('default')
x=df1

x1=x.index.tolist()
y1=x.tolist()

plt.figure(figsize=(10,5), facecolor='white')
plt.plot(x1, y1, marker='o')
plt.title('fecha vs reportes')
plt.xlabel('Fecha')
plt.ylabel('Pruebas')
plt.grid(True)
plt.savefig('grafico.png', dpi=300, bbox_inches='tight')
