import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

root_path ="C:\\Users\\acer\\Desktop\\python\\Excel\\AnalisisA.xlsx"
df = pd.read_excel(root_path, sheet_name='Linea1')

#cantidad=df[['NOMBRE SEMILLERO']]

#a=pd.value_counts(cantidad['NOMBRE SEMILLERO'])
#print(a)

#print(100 * cantidad['NOMBRE SEMILLERO'].value_counts() /75 )

#plot = cantidad['NOMBRE SEMILLERO'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            #figsize=(6, 6), shadow=True, startangle=90,
                                            #title='Porcentaje de participación por lineas Metro')
#plt.show()

T= df[['PREGUNTA 1 entrada','PREGUNTA 1 salida','PREGUNTA 2 Entrada','PREGUNTA 2 salida','PREGUNTA 3 Entrada','PREGUNTA 3 salida',
'PREGUNTA 4 Entrada','PREGUNTA 4 salida','PREGUNTA 5 Entrada','PREGUNTA 5 salida','PREGUNTA 8 Entrada','PREGUNTA 8 salida']]


colores=['#196F3D','#FF5733']   
coloret=['#196F3D','#6495ED','#F1C40F','#FF5733']

#Pregunta 1

print(100 * T['PREGUNTA 1 entrada'].value_counts() /13)
print(100 * T['PREGUNTA 1 salida'].value_counts() /13)


#plot = (100 * T['PREGUNTA 1 entrada'].value_counts()/26).plot(
#kind='bar', title= 'Cuidado de sí mismo \n Entrada', color=colores)

#plt.show()

#plot = (100 * T['PREGUNTA 1 salida'].value_counts()/26).plot(
#kind='bar', title= 'Cuidado de sí mismo \n Salida', color=colores)

#plt.show()

#Pregunta2

print(100 * T['PREGUNTA 2 Entrada'].value_counts() /13)
print(100 * T['PREGUNTA 2 salida'].value_counts() /13)

#plot = (100 * T['PREGUNTA 2 Entrada'].value_counts()/75).plot(
#kind='bar', title= 'Formación Ciudadana \n Entrada', color=colores)

#plt.show()

#plot = (100 * T['PREGUNTA 2 salida'].value_counts()/75).plot(
#kind='bar', title= 'Formación ciudadana \n Salida', color=colores)

#plt.show()

#Pregunta3

print(100 * T['PREGUNTA 3 Entrada'].value_counts() /13)
print(100 * T['PREGUNTA 3 salida'].value_counts() /13)

#plot = (100 * T['PREGUNTA 3 Entrada'].value_counts()/75).plot(
#kind='bar', title= 'Comunicación asertiva \Entrada', color=colores)

#plt.show()

#plot = (100 * T['PREGUNTA 3 salida'].value_counts()/75).plot(
#kind='bar', title= 'Comunicación asertiva \n Salida', color=colores)

#plt.show()

#Pregunta 4

print(100 * T['PREGUNTA 4 Entrada'].value_counts() /13)
print(100 * T['PREGUNTA 4 salida'].value_counts() /13)

#plot = (100 * T['PREGUNTA 4 Entrada'].value_counts()/75).plot(
#kind='bar', title= 'Cuidado del otro \n Entrada', color=colores)

#plt.show()

#plot = (100 * T['PREGUNTA 4 salida'].value_counts()/75).plot(
#kind='bar', title= 'Cuidado del otro \n Salida', color=colores)

#plt.show()

#Pregunta 5

print(100 * T['PREGUNTA 5 Entrada'].value_counts() /13)
print(100 * T['PREGUNTA 5 salida'].value_counts() /13)

#plot = (100 * T['PREGUNTA 5 Entrada'].value_counts()/75).plot(
#kind='bar', title= 'Cuidado del medio ambiente \n Entrada', color=coloret)

#plt.show()

#plot = (100 * T['PREGUNTA 5 salida'].value_counts()/75).plot(
#kind='bar', title= 'Cuidado del medio ambiente \n Salida', color=coloret)

#plt.show()

#Pregunta 8

print(100 * T['PREGUNTA 8 Entrada'].value_counts() /13)
print(100 * T['PREGUNTA 8 salida'].value_counts() /13)

#plot = (100 * T['PREGUNTA 8 Entrada'].value_counts()/75).plot(3
#kind='bar', title= 'Corresponsabilidad \n Entrada', color=colores)

#plt.show()

#lot = (100 * T['PREGUNTA 8 salida'].value_counts()/75).plot(
#ind='bar', title= 'Corresponsabilidad \n Salida', color=colores)
#plt.show()

