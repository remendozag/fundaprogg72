print('Programa Ordenamiento Insercion')
tamanio=int(input('Digite tamaño del vector:'))
vector=[]
for conta_i in range(0,tamanio, 1):
    elemento=int(input('Digite elemento:'))
    vector.append(elemento) #15
print(vector)
#ALGORITMO METODO DE INSERCION
for conta_i in range(1,tamanio):
    temporal=vector[conta_i] #33
    conta_j=conta_i-1 #0
    while temporal<vector[conta_j-1] and conta_j>0:
        vector[conta_j]=vector[conta_j-1] #15
        conta_j=conta_j-1
    vector[conta_j]=temporal

print(vector)
