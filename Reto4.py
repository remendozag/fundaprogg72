#RETO 4
def ordenamientoBurbuja(vector,tamanio):
    #ALGORITMO ORDENAMIENTO POR INTERCAMBIO O BURBUJA
    for conta_i in range(1,tamanio):
        for conta_j in range(0,tamanio-1):
            if vector[conta_j]>vector[conta_j+1]:
                temporal=vector[conta_j]
                vector[conta_j]=vector[conta_j+1]
                vector[conta_j+1]=temporal
    print(vector)

#ENTRADAS
if __name__=='__main__':
    cantidadProducto=int(input()) #2
    productoSinIva=0
    productoConIva=0
    totalProductosSinIVA=0
    totalProductosConIVA=0
    codigos=[]
    nombres=[]
    cantidades=[]
    valores=[]
    tiposIVA=[]
    for contador in range(0,cantidadProducto,1):
        codigos.append(int(input()))
        nombres.append(input())
        cantidades.append(int(input()))
        valores.append(float(input()))
        tiposIVA.append(int(input()))
        for contador in range(0,cantidadProducto,1):
            print(codigos[contador])
            print(nombres[contador])
            productoSinIva=cantidades[contador]*valores[contador]
            print(productoSinIva)
            if tiposIVA[contador]==1:
                productoConIva=productoSinIva
            elif tiposIVA[contador]==2:
                productoConIva=productoSinIva+(productoSinIva*0.05)
            elif tiposIVA[contador]==3:
                productoConIva=productoSinIva+(productoSinIva*0.19)
        print(productoConIva)
        totalProductosSinIVA+=productoSinIva
        totalProductosConIVA+=productoConIva
    print(totalProductosConIVA)
    impuestoIVA=totalProductosConIVA-totalProductosSinIVA
    print(impuestoIVA)