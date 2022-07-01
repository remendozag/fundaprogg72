print('Programa Ordenamiento Seleccion')
tamanio=int(input('Digite tamaño del vector:'))
vector=[]
for conta_i in range(0,tamanio, 1):
    elemento=int(input('Digite elemento:'))
    vector.append(elemento) #15
print(vector)
vector2=[]
vector2=list(vector)
#ALGORITMO ORDENAMIENTO POR SELECCION
for conta_i in range(0,tamanio):
    temporal=vector[conta_i] #15
    indice_k=conta_i #0
    for conta_j in range(conta_i+1,tamanio):
        if vector[conta_j]<temporal:
            temporal=vector[conta_j] #10
            indice_k=conta_j #3
    vector[indice_k]=vector[conta_i] #15
    vector[conta_i]=temporal

print(vector)
print(vector2)
vector2.sort()
print(vector2)


