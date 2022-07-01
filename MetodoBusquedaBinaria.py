print('Programa Busqueda Binaria')
tamanio=int(input('Digite tamaño del vector:'))
vector=[]
for conta_i in range(0,tamanio, 1):
    elemento=int(input('Digite elemento:'))
    vector.append(elemento) #15
print(vector)
vector.sort()
print(vector)

#ALGORITMO DE BUSQUEDA BINARIA
numeroBuscar=int(input('Digite numero a buscar:'))
inferior=0
superior=tamanio
while True:
    centro=int((inferior+superior)/2)
    if vector[centro]<numeroBuscar:
        inferior=centro+1
    elif vector[centro]>numeroBuscar:
        superior=centro-1
    elif inferior>superior or vector[centro]==numeroBuscar:
        if vector[centro]==numeroBuscar:
            print('Numero: ',numeroBuscar,'Posicion: ',centro)
            break
        else:
            print('Numero: ',numeroBuscar,'No esta')
            break