#EXCEPCIONES
numero1=int(input('Digite dividendo:'))
numero2=int(input('Digite divisor:'))

#raise ZeroDivisionError('No se puede dividir entre cero')
'''
if numero2!=0:
    division=numero1/numero2 #0
    print(division)
else:
    print('No se puede dividir entre cero') #ZeroDivisionError: division by zero
'''
#TRY EXCEPT
try:
    division=numero1/numero2 #0
    print(division)
except ZeroDivisionError:
    print('No se puede dividir entre cero')
