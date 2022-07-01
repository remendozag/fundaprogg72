#ENTRADAS
cantidadProducto=int(input()) #2
productoSinIva=0
productoConIva=0
totalProductosSinIVA=0
totalProductosConIVA=0
for contador in range(0,cantidadProducto,1):
    codigoProducto=int(input())
    nombreProducto=input()
    cantidadComprada=int(input())
    valorUnitario=float(input())
    tipoIVA=int(input())
    productoSinIva=cantidadComprada*valorUnitario
    if tipoIVA==1:
        productoConIva=productoSinIva
    elif tipoIVA==2:
        productoConIva=productoSinIva+(productoSinIva*0.05)
    elif tipoIVA==3:
        productoConIva=productoSinIva+(productoSinIva*0.19)
    totalProductosSinIVA+=productoSinIva
    totalProductosConIVA+=productoConIva
    print(codigoProducto)
    print(nombreProducto)
    print(productoSinIva)
    print(productoConIva)
print(totalProductosConIVA)
impuestoIVA=totalProductosConIVA-totalProductosSinIVA
print(impuestoIVA)