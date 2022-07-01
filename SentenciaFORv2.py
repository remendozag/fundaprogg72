'''
Escribir un programa que lea 5 notas de tripulantes
y nos informe cuántos tienen notas mayores o
iguales a 3 y cuántos menores.
Para resolver este problema se requieren tres contadores
'''
notasMayores=0
notasMenores=0
for contador in range(1,6):
    nota=float(input(f'Digite nota {contador}:'))
    if nota>=3:
        notasMayores+=1
    else:
        notasMenores+=1
print('La notas mayores:',notasMayores)
print('La notas menores:',notasMenores)