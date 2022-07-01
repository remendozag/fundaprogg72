#ENTRADA
sueldo=float(input('Digite sueldo:'))
#PROCESO
if sueldo>=2000000:
    print('Debe declarar Impuesto')
else:
    print('No debe declarar Impuesto')

#DIA SIN IVA
#ENTRADA
print('Programa dia SIN IVA')
producto=float(input('Digite producto con IVA:'))
#PROCESO
if producto<=2900000:
    totalSinIVA=producto-(producto*0.19)
    print('Exentos de Impuesto:', totalSinIVA)
else:
    totalConIVA=producto+(producto*0.19)
    print('Pagar IVA 19%', totalConIVA)
