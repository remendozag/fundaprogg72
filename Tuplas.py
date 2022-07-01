#TUPLAS O TUPLES
tupla=()
print(type(tupla))
print(tupla)
tupla2=(1,2,3)
print(tupla2)
#SLICES
print(tupla2[0])
print(tupla2[1])
print(tupla2[2])
#INMUTABLE
#tupla2[0]=2 #error
#FOR
for iterador in range(len(tupla2)):
    print(tupla2[iterador])
#FOR EACH
for elemento in tupla2:
    print(elemento)
print('Tupla como Lista')
lista=list(tupla2)
for elemento in lista:
    print(elemento)
print(lista)
tupla3=tuple(lista)
print(tupla3)
cantantesHombres=(1,'Juan Esteban Aristizabal Vasquez', 49, 1.72)
#cantantesHombres[2]=50
print(type(cantantesHombres))
print(cantantesHombres)
#OPERACIONES
#tupla2=(1,2,3)
tupla4=(4,5,6)
resultado=tupla2+tupla4
print(resultado)
x,y,z=tupla4
print(x,y,z)
coordenada2D=(4,5)
coordenada3D=(1,2,3)
print(tupla4)
conteo=tupla4.count(4)
print(conteo)
indice=tupla4.index(4)
print(indice)
lista2=list(tupla2) #(1,2,3) [1,2,3]
print(lista2)
lista4=list(tupla4) #(4,5,6) [4,5,6]
print(lista4)
listaSuma=[] #[5,7,9]
for iterador in range(len(lista2)):
    listaSuma.append(lista2[iterador]+lista4[iterador])
    #print(listaSuma[iterador])
print(listaSuma)