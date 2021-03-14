
import pandas as pd
import matplotlib.pyplot as plt

workbook1 ="C:\\Users\\acer\\Desktop\\python\\Excel\\Analisis_AutoEvaluacion_Adolescentes.xlsx"

df = pd.read_excel(workbook1, sheet_name='Hoja1')


valores = df[["NOMBRE SEMILLERO","PREGUNTA 1 entrada","PREGUNTA 1 salida"]]
#print(valores)
#print(valores.head(76))
#print(pd.value_counts(valores['NOMBRE SEMILLERO']))
#print(pd.value_counts(valores['PREGUNTA 1 entrada']))
#print(pd.value_counts(valores['PREGUNTA 1 salida']))
#fig, ax = plt.subplots()
#ax.plot(df["PREGUNTA 5 Entrada"], df["PREGUNTA 5 salida"])
#plt.show()

#print(100 * valores['PREGUNTA 1 entrada'].value_counts() / len(valores['PREGUNTA 1 entrada']))
#print(100 * valores['PREGUNTA 1 salida'].value_counts() / len(valores['PREGUNTA 1 salida']))


#ax= valores.plot.bar()
#ax2=ax.twinx
#plt.show()
#-------------------------------Valores numericos--------------------

val = df[["PREGUNTA 5 Entrada","PREGUNTA 5 salida"]]

print(100 * val['PREGUNTA 5 Entrada'].value_counts() / len(val['PREGUNTA 5 Entrada']))
print(100 * val['PREGUNTA 5 salida'].value_counts() / len(val['PREGUNTA 5 salida']))


# Gráfico de barras semilleros
#plot = valores['NOMBRE SEMILLERO'].value_counts().plot(kind='bar',
                                            #title='Semilleros Amigos Metro')



# Gráfico de barras de pasajeros del Titanic
plot = val['PREGUNTA 5 Entrada'].value_counts().plot(kind='bar',
                                            title='Datos entrada pregunta 5')
plt.show()

#---------------------------Torta-----------------------------
plot = valores['PREGUNTA 1 entrada'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            figsize=(6, 6),
                                            title='Estoy montando en bicicleta y no estoy pendiente cuando aparecen carros y las motoalgien me recomienda mirar ¿le hago caso?')
plt.show()