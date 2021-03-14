import pandas as pd
import matplotlib.pyplot as plt

workbook1 ="C:\\Users\\acer\\Desktop\\python\\Excel\\Analisis_AutoEvaluacion_Adolescentes.xlsx"

df = pd.read_excel(workbook1, sheet_name='Hoja1')
valores = df[['NOMBRE SEMILLERO', 'PREGUNTA 1 entrada', 'PREGUNTA 1 salida']]
valores1= df[['PREGUNTA 7 Entrada', 'PREGUNTA 7 salida']]

#print(valores.head(25))

#Tabla de frecuencia
#Conteo de datos

#a=pd.value_counts(valores['NOMBRE SEMILLERO'])
#b=pd.value_counts(valores['PREGUNTA 1 entrada'])
#c=pd.value_counts(valores['PREGUNTA 1 salida'])
#print(a)
#plot = valores['NOMBRE SEMILLERO'].value_counts().plot(kind='bar',title='Semilleros')
#plt.show()
#print(b)
#print(c)

#-----------------
e=pd.value_counts(valores1['PREGUNTA 7 Entrada'])
s=pd.value_counts(valores1['PREGUNTA 7 salida'])
print(e)
print(s)
#plot = valores1['PREGUNTA 7 Entrada'].value_counts().plot(kind='bar', title='Datos de entrada pregunta 7')
#plt.show()

b=pd.crosstab(index=valores1['PREGUNTA 7 Entrada'],
            columns=valores1['PREGUNTA 7 salida'], margins=True)
print(b)
c=pd.crosstab(index=valores1['PREGUNTA 7 Entrada'], columns=valores1['PREGUNTA 7 salida'],
            margins=True).apply(lambda r: r/r.sum() *100,
                                axis=1)

print(c)

plot = pd.crosstab(index=valores1['PREGUNTA 7 Entrada'],
            columns=valores1['PREGUNTA 7 salida']).apply(lambda r: r/r.sum() *100,
                                              axis=1).plot(kind='bar')
plt.show()