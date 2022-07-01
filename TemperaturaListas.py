'''
Queremos guardar la temperatura mínima y máxima
de 5 días. Realiza un  programa que de la siguiente
información:
La temperatura media de cada día  Los días con menos
temperatura
Se lee una temperatura por teclado y se  muestran los
días cuya temperatura  máxima coincide con ella
si no existe  ningún día se muestra un mensaje de
información.
'''
#import datetime from date, time, datetime
#from numpy as np
diasSemana=['lunes','martes','miercoles','jueves','viernes']
temperaturaMinima=[17,18,20,24,22]
temperaturaMaxima=[24,18,25,23,40]
#Ciclo foreach
suma=0
for iterador in range(0,len(temperaturaMinima),1): #range(start,stop,step)
    suma+=temperaturaMinima[iterador]
    media=suma/len(temperaturaMinima)

print('Promedio de Temperatura Minima es:', media)

suma=0
for iterador in range(0,len(temperaturaMaxima),1): #range(0,len(temperaturaMinima),1) range(start,stop,step)
    suma+=temperaturaMaxima[iterador]
    media=suma/len(temperaturaMaxima)

print('Promedio de Temperatura Maxima es:', media)

temperaturaMaxSemana=max(temperaturaMaxima)
print(temperaturaMaxSemana)
temperaturaMinSemana=min(temperaturaMinima)
print(temperaturaMinSemana)

for iterador in range(0,len(temperaturaMaxima),1): #range(0,len(temperaturaMinima),1) range(start,stop,step)
    if temperaturaMaxSemana==temperaturaMaxima[iterador]:
        print(diasSemana[iterador])





