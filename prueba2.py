import pandas as pd
import matplotlib.pyplot as plt

workbook1 ="C:\\Users\\acer\\Desktop\\python\\Excel\\Analisis_AutoEvaluacion_Adolescentes.xlsx"

df = pd.read_excel(workbook1, sheet_name='Hoja1')
datos = df[["PREGUNTA 8 Entrada","PREGUNTA 7 Entrada"]]
datos1 = df[["PREGUNTA 8 salida", "PREGUNTA 7 salida"]] 
print(pd.crosstab(index=datos['PREGUNTA 7 Entrada'], columns=datos1['PREGUNTA 7 salida'], margins=True))

print(pd.value_counts(datos['PREGUNTA 7 Entrada']))
print(pd.value_counts(datos1['PREGUNTA 7 salida']))

plot = pd.crosstab(index=datos['PREGUNTA 7 Entrada'],
            columns=datos1['PREGUNTA 7 salida']).apply(lambda r: r/r.sum() *100,
                                              axis=1).plot(kind='bar')
plt.show()
#print(100 * datos['PREGUNTA 8 Entrada'].value_counts() / len(datos['PREGUNTA 8 Entrada']))
#print(100 * datos['PREGUNTA 8 salida'].value_counts() / len(datos['PREGUNTA 8 salida']))

#plot = datos['PREGUNTA 8 Entrada'].value_counts().plot(kind='bar',
                                            #title='Datos pregunta 8')

#plot = datos['PREGUNTA 8 salida'].value_counts().plot(kind='bar',
                                            #title='Datos pregunta 8')
#plt.show()


