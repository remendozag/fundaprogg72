def busquedaBinariaRecur(vector,numero,inferior,superior):
    #CONDICION DE SALIDA
    if inferior>superior:
        return -1
    centro=(inferior+superior)//2 #DIVISION ENTERA
    try:
        if vector[centro]==numeroBuscar:
            return centro
        elif vector[centro]<numeroBuscar:
            #inferior=centro+1
            return busquedaBinariaRecur(vector,numero,centro+1,superior)
        elif vector[centro]>numeroBuscar:
            #superior=centro-1
            return busquedaBinariaRecur(vector,numero,inferior,centro-1)
    except IndexError:
        return 'Numero no encontrado'


def llenarVector(tamanio):
    vector=[]
    for conta_i in range(0,tamanio, 1):
        elemento=int(input('Digite elemento:'))
        vector.append(elemento)
    vector.sort() #[5,4,3,2,1]
    return vector #[1,2,3,4,5]


if __name__=='__main__':
    print('Busqueda Binaria Recursiva')
    tamanio=int(input('Digite tamaño del vector:')) #5
    vectorOrd=llenarVector(tamanio) #[1,2,3,4,5]
    print(vectorOrd)
    numeroBuscar=int(input('Digite numero a buscar:')) #4
    inferior=0
    superior=tamanio #5
    print(busquedaBinariaRecur(vectorOrd,numeroBuscar,inferior,superior))