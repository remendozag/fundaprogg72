#SLICES (CORTES)
mi_slice='programacion'
print(mi_slice)
print(mi_slice[3])
print(mi_slice[-9])
print(mi_slice[0:8])
print(mi_slice[:8])
#LISTA
lista=[] #lista vacia
mi_lista=[1,2,3]
print(type(mi_lista))
print(mi_lista)
print(mi_lista[0]) #1
print(mi_lista[1]) #2
print(mi_lista[2]) #3
print(mi_lista[-3]) #1
print(mi_lista[-2]) #2
print(mi_lista[-1]) #3
otra_lista=list(mi_lista)
print(otra_lista)
#print(id(mi_lista))
#print(id(otra_lista))
mi_lista.append(4)
print(mi_lista) #[1,2,3,4]
print(otra_lista)
longitud=len(mi_lista)
print(longitud) #4
for contador in range(0,len(mi_lista),1):
    print(mi_lista[contador])
#MUTABILIDAD
mi_lista[3]=5
print(mi_lista)
inventario=[1,'Manzana',1200.0, 200]
print(inventario[1], inventario[3])


