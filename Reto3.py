#ENTRADAS
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
    codigoProducto=int(input())
    codigos.append(codigoProducto)
    nombreProducto=input()
    nombres.append(nombreProducto)
    cantidadComprada=int(input())
    cantidades.append(cantidadComprada)
    valorUnitario=float(input())
    valores.append(valorUnitario)
    tipoIVA=int(input())
    tiposIVA.append(tipoIVA)

#SALIDAS
print(len(codigos))
print(len(nombres))
print(len(cantidades))
print(len(valores))
print(len(tiposIVA))
totalProductosSinIVA=0
totalProductosConIVA=0
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





