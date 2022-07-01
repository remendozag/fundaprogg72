'''
Una planta que fabrica perfiles de hierro
posee un lote de n piezas.
Confeccionar un programa que pida ingresar
por teclado la cantidad de piezas a procesar
y luego ingrese la longitud de cada perfil;
sabiendo que la pieza cuya longitud esté
comprendida en el rango de 1,20 y 1,30 son aptas.
Imprimir por pantalla la cantidad de
piezas aptas que hay en el lote.
'''
#ENTRADAS
cantidad=int(input('Digite cantidad de piezas:')) #2
#PROCESO
piezasAptas=0
piezasNoAptas=0
contador=0 #inicializador
while contador<cantidad: #condicional
    longitud=float(input('Digite longitud:'))
    if longitud>=1.2 and longitud<=1.3: #1.2 <= longitud <=1.3
        print('Son aptas')
        piezasAptas+=1 #piezasAptas=piezasAptas+1
    else:
        print('No son aptas')
        piezasNoAptas+=1
    contador+=1 #contador=contador+1
print('La cantidad de piezas aptas:',piezasAptas)
print('La cantidad de piezas no aptas:',piezasNoAptas)

