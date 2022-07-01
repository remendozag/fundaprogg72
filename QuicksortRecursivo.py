def quicksortRecursivo(vector):
    if len(vector)<2:
        return vector
    else:
        #ASIGNACION MULTIPLE
        menores, pivote, mayores=particion(vector) #([1, 5, 4, 6, 2, 7], 8, [14, 15, 12, 11, 10, 9])
        return quicksortRecursivo(menores)+[pivote]+quicksortRecursivo(mayores)


def particion(vector):
    pivote=vector[0] #8
    menores=[]
    mayores=[]
    for conta_i in range(1,len(vector),1):
        if vector[conta_i]<pivote:
            menores.append(vector[conta_i])
        else:
            mayores.append(vector[conta_i])
    return menores, pivote, mayores


def llenarVector(tamanio):
    vector=[]
    for conta_i in range(0,tamanio, 1):
        elemento=int(input('Digite elemento:'))
        vector.append(elemento)
    return vector #[1,2,3,4,5]

if __name__=='__main__':
    print('Programa Quicksort Recursiva')
    tamanio=int(input('Digite tamaño del vector:')) #5
    vector=llenarVector(tamanio) #[1,2,3,4,5]
    print(vector)
    #print(particion(vector))
    print(quicksortRecursivo(vector))
