'''
Realizar un programa que acumule (sume) valores
ingresados por teclado hasta ingresar el 9999
(no sumar dicho valor, indica que ha finalizado la carga).
Imprimir el valor acumulado e informar si dicho
valor es cero, mayor a cero o menor a cero.
'''
suma=0
while True:
    numero=int(input('Digite numero:'))
    if numero==9999:
        break
    suma+=numero #suma=suma+numero
print(f'La suma es:{suma}') #'La suma es:',suma