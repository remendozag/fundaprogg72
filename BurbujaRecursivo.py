def ordenamientoBurbujaRecursivo(vector, ordenado, tamanio):
    if not ordenado:
        ordenado=True
        for conta_j in range(0,tamanio-1):
            if vector[conta_j]>vector[conta_j+1]:
                temporal=vector[conta_j]
                vector[conta_j]=vector[conta_j+1]
                vector[conta_j+1]=temporal
                ordenado=False
        ordenamientoBurbujaRecursivo(vector, ordenado, tamanio)
    else:
        print(vector)


def llenarVector(tamanio): #5
    vector=[]
    for conta_i in range(tamanio):
        elemento=int(input('Digite elemento:'))
        vector.append(elemento)
    return vector #[5,4,3,2,1]

#METODO PRINCIPAL
if __name__=='__main__':
    print('Ordenamiento Burbuja Recursivo')
    tamanio=int(input('Digite tamaño vector:'))#5
    vectorDesordenado=llenarVector(tamanio) #[5,4,3,2,1]
    print(vectorDesordenado)
    ordenado=False
    ordenamientoBurbujaRecursivo(vectorDesordenado, ordenado, tamanio)

