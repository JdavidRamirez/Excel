import pandas as pd
import matplotlib.pyplot as plt

root_path ="C:\\Users\\acer\\Desktop\\python\\Excel\\Estadisticas.xlsx"
df = pd.read_excel(root_path, sheet_name='Guía virtual')
datos = df[['Fecha','T','Evaluacion','IE','Pregunta','Escala']]

#Nombre de las columnas 
print(df.columns)

print(df.shape)

#print(datos.head(10))

#print(pd.value_counts(datos['T']))
#a=len(datos['T'])/5
#print(100*(pd.value_counts(datos['T'])/1000))
#print(pd.value_counts(datos['IE']))
#plot=datos['IE'].value_counts().plot(kind='bar', title='Instituciones educativas')
#plt.show()
#z=pd.crosstab(index=datos['Pregunta'], columns=datos['Escala'], margins=True)
#print(z)
#plot= pd.crosstab(index=datos['Escala'], columns=datos['Pregunta']).apply(lambda r: r/r.sum()*100, axis=1).plot(kind='bar')
#plt.show()
