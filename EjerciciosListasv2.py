equipos=['Tolima','Junior','Cali','Nacional']
resultados=[2,0,5,0]
apuesta=float(input('Digite apuesta:'))

for indice in range(0,len(equipos),2):
    if resultados[indice]>resultados[indice+1]:
        print(f'El ganador es:{equipos[indice]}')
        dineroGanado=apuesta*10
        print('Gano:',dineroGanado)
    else:
        print(f'El ganador es:{equipos[indice+1]}')
        dineroGanado=apuesta*10
        print('Gano:',dineroGanado)