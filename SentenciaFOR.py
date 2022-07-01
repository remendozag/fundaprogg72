'''
Escribir un programa que lea n números enteros
y calcule la cantidad de valores mayores o iguales
a 1000.
'''
#ENTRADAS
cantidad=int(input('Digite cantidad de números:'))
#PROCESO
mayores=0
menores=0
for iterador in range(0,cantidad,1):
    numero=int(input('Digite número:'))
    if numero>=1000:
        mayores+=1
    else:
        menores+=1
print('Los mayores son:', mayores)
print('Los menores son:', menores)

