'''
Se ingresan cinco notas(Retos) de un tripulante, 
si el promedio es mayor o igual a tres 
mostrar un mensaje "Certificado".

#ENTRADAS
nota1=0.0
nota2=0.0
nota3=0.0
nota4=0.0
nota5=0.0
nota1=float(input("Digite nota 1:"))
nota2=float(input("Digite nota 2:"))
nota3=float(input("Digite nota 3:"))
nota4=float(input("Digite nota 4:"))
nota5=float(input("Digite nota 5:"))
#PROCESO
promedio=(nota1+nota2+nota3+nota4+nota5)/5
print('El promedio es:',promedio)
if promedio>=3:
    #SALIDA
    print('Certificado')
else:
    print('No Certificado')
'''
'''
Realizar un programa que lea por teclado dos números, 
si el primero es mayor al segundo informar su suma y diferencia, 
en caso contrario informar el producto y la división del primero 
respecto al segundo.
'''
#ENTRADAS
numero1=0.0
numero2=0.0
numero1=float(input('Digite numero 1:'))
#print(type(numero1))
#print(numero1)
numero2=float(input('Digite numero 2:'))
#print(type(numero2))
#print(numero2)
#PROCESO
if numero1>numero2:
    #SALIDA
    suma=numero1+numero2
    print('La suma es:',suma)
    diferencia=numero1-numero2
    print('La diferencia es:',diferencia)
elif numero1<numero2:
    #SALIDA
    producto=numero1*numero2
    print('El producto es:',producto)
    division=numero1/numero2
    print('La division es:',division)
elif numero1==numero2:
    exponente=numero1**numero2
    print('El exponente es:', exponente)
    modulo=numero1%numero2
    print('El modulo es:', modulo)
else:
    print('Fuera de rango')

