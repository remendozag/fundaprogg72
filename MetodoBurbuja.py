print('Programa Ordenamiento Intercambio o Burbuja')
tamanio=int(input('Digite tamaño del vector:'))
vector=[]
for conta_i in range(0,tamanio, 1):
    elemento=int(input('Digite elemento:'))
    vector.append(elemento) #15
print(vector)
iteraciones_i=0
iteraciones_j=0
#ALGORITMO ORDENAMIENTO POR INTERCAMBIO O BURBUJA
for conta_i in range(1,tamanio):
    iteraciones_i+=1
    for conta_j in range(0,tamanio-1):
        iteraciones_j+=1
        if vector[conta_j]>vector[conta_j+1]:
            temporal=vector[conta_j]
            vector[conta_j]=vector[conta_j+1]
            vector[conta_j+1]=temporal
print(iteraciones_i)
print(iteraciones_j)
print(vector)


