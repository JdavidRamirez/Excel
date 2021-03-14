import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

root_path ="C:\\Users\\acer\\Desktop\\python\\Excel\\Analisis.xlsx"
df = pd.read_excel(root_path, sheet_name='Cuenca6')

#a=pd.value_counts(lineas['NOMBRE SEMILLERO'])
#print(a)

#print(100 * lineas['NOMBRE SEMILLERO'].value_counts() /233 )

#plot = lineas['NOMBRE SEMILLERO'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            #figsize=(6, 6), shadow=True, startangle=90,
                                            #title='Porcentaje de participación por lineas Metro')
#plt.show()


Linea6=df[['PREGUNTA 1 entrada','PREGUNTA 1 salida','PREGUNTA 2 Entrada','PREGUNTA 2 salida','PREGUNTA 3 Entrada','PREGUNTA 3 salida',
'PREGUNTA 4 Entrada','PREGUNTA 4 salida','PREGUNTA 5 Entrada','PREGUNTA 5 salida','PREGUNTA 6 Entrada','PREGUNTA 6 salida']]

colores=['#008080','#9A2A2A']   
coloret=['#0E6655','#DAF7A6','#FFC300','#FF5733']

plot=Linea6['PREGUNTA 1 entrada'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            figsize=(6, 6),shadow=True,startangle=90, colors=colores,
                                            title='Cuidado de mi mismo')


plt.show()

plot=Linea6['PREGUNTA 1 salida'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            figsize=(6, 6),shadow=True,startangle=90, colors=colores,
                                            title='Cuidado de mi mismo')


plt.show()

plot=Linea6['PREGUNTA 2 Entrada'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            figsize=(6, 6),shadow=True,startangle=90, colors=colores,
                                            title='Formación ciudadana  ')


plt.show()

plot=Linea6['PREGUNTA 2 salida'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            figsize=(6, 6),shadow=True,startangle=90, colors=colores,
                                            title='Formación ciudadana')
plt.show()

plot=Linea6['PREGUNTA 3 Entrada'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            figsize=(6, 6),shadow=True,startangle=90, colors=colores,
                                            title='Comunicación asertiva')
plt.show()

plot=Linea6['PREGUNTA 3 salida'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            figsize=(6, 6),shadow=True,startangle=90, colors=colores,
                                            title='Comunicación asertiva')
plt.show()

plot=Linea6['PREGUNTA 4 Entrada'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            figsize=(6, 6),shadow=True,startangle=90, colors=colores,
                                            title='Consideración por el otro')
plt.show()

plot=Linea6['PREGUNTA 4 salida'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            figsize=(6, 6),shadow=True,startangle=90, colors=colores,
                                            title='Consideración por el otro')
plt.show()

#----------------------------------------Datos nuemricos-----------------------#
print(100 * Linea6['PREGUNTA 5 Entrada'].value_counts() /17)
print(100 * Linea6['PREGUNTA 5 salida'].value_counts() / 17)

print(100 * Linea6['PREGUNTA 6 Entrada'].value_counts() /17)
print(100 * Linea6['PREGUNTA 6 salida'].value_counts() /17)



plot = (100 * Linea6['PREGUNTA 5 Entrada'].value_counts()/17).plot(
kind='bar', title= '% Cuidado del medio ambiente / Entrada', color=coloret)

plt.show()

plot = (100 * Linea6['PREGUNTA 5 salida'].value_counts() /17).plot(
kind='bar', title= '% Cuidado del medio ambiente / Salida', color=coloret)

plt.show()

plot = (100 * Linea6['PREGUNTA 6 Entrada'].value_counts() /17).plot(
kind='bar', title= '% Corresponsabilidad / Entrada', color=coloret)

plt.show()

plot = (100 * Linea6['PREGUNTA 6 salida'].value_counts() /17).plot(
kind='bar', title= '% Corresponsabilidad / Salida', color=coloret)

plt.show()