import pandas as pd
import matplotlib.pyplot as plt

root_path ="C:\\Users\\acer\\Desktop\\python\\Excel\\Analisis.xlsx"
df = pd.read_excel(root_path, sheet_name='Hoja2')

datos = df[["Total"]]
#a=pd.value_counts(datos['Total'])
#print(a)

#b=100 * datos['Total'].value_counts() / len(datos['Total'])
#print(b)


# Gráfico de barras total


#plot = datos['Total'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            #figsize=(6, 6),
                                            #title='Porcentaje de respuestas')
#plt.show()

#Grafico de variaciones

#variacion= df[['Variacion']]

#c=100 * variacion['Variacion'].value_counts() / len(variacion['Variacion'])
#print(c)

#plot=variacion['Variacion'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            #figsize=(6, 6),
                                            #title='Porcentaje de Variacion', colors=['#00B050','#0070C0','#FFFF00','#FF0000'])
#plt.show()

p6=df[['PREGUNTA 6 Entrada', 'PREGUNTA 6 salida']]

print(100 * p6['PREGUNTA 6 Entrada'].value_counts() / 233)
print(100 * p6['PREGUNTA 6 salida'].value_counts() / 233)

plot=p6['PREGUNTA 6 Entrada'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            figsize=(6, 6),
                                            title='Corresponsabilidad', colors=['#00B050','#0070C0','#FFFF00','#FF0000'])
plt.show()

plot=p6['PREGUNTA 6 salida'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            figsize=(6, 6),
                                            title='Corresponsabilidad', colors=['#00B050','#0070C0','#FFFF00','#FF0000'])
plt.show()
#plot = (100 * variacion['Variacion'].value_counts() / len(variacion['Variacion'])).plot(
#kind='bar', title='Variacion %', color='Cyan')



#plt.show()

p1= df[['PREGUNTA 1 entrada', 'PREGUNTA 1 salida']]

#a=pd.value_counts(p1['PREGUNTA 1 entrada'])
#b=pd.value_counts(p1['PREGUNTA 1 salida'])
#print(a)
#print(b)


#print(100 * p1['PREGUNTA 1 entrada'].value_counts() / 233)
#print(100 * p1['PREGUNTA 1 salida'].value_counts() / 233)

#plot=p1['PREGUNTA 1 entrada'].value_counts().plot(kind='pie', autopct='%.2f', 
                                           # figsize=(6, 6),
                                           # title='Autocuidado')
#plot=p1['PREGUNTA 1 entrada'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            #figsize=(6, 6),
                                            #title='Autocuidado')
#plt.show()
#plot=p1['PREGUNTA 1 salida'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            #figsize=(6, 6),
                                            #title='Autocuidado')

#plot = pd.crosstab(index=p1['PREGUNTA 1 entrada'],
            #columns=p1['PREGUNTA 1 salida']).apply(lambda r: r/r.sum() *100,
                                              #axis=1).plot(kind='bar')
#plt.show()

#d=pd.crosstab(index=p1['PREGUNTA 1 entrada'], columns=p1['PREGUNTA 1 salida'],margins=True).apply(lambda r: r/233 *100,axis=1)
#print(d)

#--------------------
#p5= df[['PREGUNTA 5 Entrada', 'PREGUNTA 5 salida']]

#print(100 * p5['PREGUNTA 5 Entrada'].value_counts() / 233)
#print(100 * p5['PREGUNTA 5 salida'].value_counts() / 233)

#plot = (100 * p5['PREGUNTA 5 Entrada'].value_counts() / 233).plot(
#kind='bar', title= '% Cuidado del medio ambiente / Entrada', color=['yellow','green','cyan','blue'])

#plt.show()

#plot = (100 * p5['PREGUNTA 5 salida'].value_counts() / 233).plot(
#kind='bar', title= '% Cuidado del medio ambiente / salida', color=['yellow','green','cyan','blue'])

#plt.show()

#plot1=p4['PREGUNTA 5 Entrada'].value_counts().plot(kind='pie', autopct='%.2f', 
                                           # figsize=(6, 6),shadow=True,startangle=90, colors=['#008363','#006383'],
                                           # title='% Consideración por el otro')


#plt.show()

#plot1=p4['PREGUNTA 4 salida'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            #figsize=(6, 6),shadow=True,startangle=90, colors=['#008363','#006383'],
                                            #title='% Consideración por el otro')
#plt.show()
#plot2=p3['PREGUNTA 3 salida'].value_counts().plot(kind='bar', autopct='%.2f', 
                                            #figsize=(6, 6),
                                            #title='% Comunicación asertiva')




# gráfico de barras de frecuencias relativas.
#plot = (100 * p3['PREGUNTA 3 Entrada'].value_counts() / 233).plot(
#kind='bar', title= '% Comunicación asertiva / Entrada', color=['Green','red'])

#plt.show()

#plot = (100 * p3['PREGUNTA 3 salida'].value_counts() / 233).plot(
#kind='bar', title= '% Comunicación asertiva / Salida', color=['Green','red'])

#plt.show()

