'''
TIPOS DE DATOS
CONDICIONALES
REPETITIVAS
ESTRUCTURAS DE DATOS
'''
#LISTAS DE LISTAS
lista1=[1,2,3]
lista2=[4,5,6]
lista3=[]
print(lista1)
print(lista2)
lista3.append(lista1)
lista3.append(lista2)
lista4=[1, 'Shakira Isabel Mebarak Ripoll',45,1.57,True]
#print(lista3)
#lista3.insert(0,2)
#print(lista3)
print(lista3) #[[1, 2, 3], [4, 5, 6]]
print(lista3[0])
print(lista3[1])
for iterador in range(0,len(lista4),1):
    print(lista4[iterador])

print(lista3)
print(lista3[0][2])
for iterador_i in range(0,len(lista3),1):
    #print(lista3[iterador_i])
    for iterador_j in range(0,3,1):
        print(lista3[iterador_i][iterador_j])

cantante0=['item', 'Nombre Completo','Edad','Altura','Soltero']
cantante1=[1, 'Shakira Isabel Mebarak Ripoll',45,1.57,True]
cantante2=[2, 'Carolina Giraldo Navarro',31,1.6,True]
cantante2[2]=32
print(cantante2)
cantantes=[]
cantantes.insert(0, cantante0)
cantantes.insert(1, cantante1)
cantantes.insert(2, cantante2)
print(cantantes) #[[1, 'Shakira Isabel Mebarak Ripoll', 45, 1.57, True],
#[2, 'Carolina Giraldo Navarro', 31, 1.6, True]]
for iterador_i in range(0,len(cantantes),1):
    #print(lista3[iterador_i])
    for iterador_j in range(0,5,1):
        print(cantantes[iterador_i][iterador_j])







