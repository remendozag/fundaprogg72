'''
Escribe un programa que lea una cadena y devuelva un diccionario
con la cantidad de apariciones de cada palabra en la cadena.
Por ejemplo, si recibe “que lindo día que hace hoy”
debe devolver: ‘que’: 2, ‘lindo’: 1, ‘día’: 1, ‘hace’: 1, ‘hoy’: 1

diccionario={} #{'que':2}
cadena=input('Digite cadena:')
lista=cadena.split(' ')
print(lista)
for iterador in lista:
    if iterador in diccionario:
        diccionario[iterador]+=1 #{'que':2}
    else:
        diccionario[iterador]=1 #{'que':1}

print(diccionario)

for clave, valor in diccionario.items():
    print(clave,':',valor)
'''
'''
Suponga un diccionario que contiene como clave el nombre de una persona 
y como valor una lista con todas sus “gustos”. Desarrolle un programa 
que agregue “gustos” a la persona:
Si la persona no existe la agregue al diccionario 
con una lista que contiene un solo elemento.
Si la persona existe y el gusto existe en su lista, 
no tiene ningún efecto.
Si la persona existe y el gusto no existe en su lista, 
agrega el gusto a la lista.
Se deja de pedir personas cuando introducimos el carácter “*”.
'''
gustos={
    #'nombre':'gusto',
}
nombre=input('Digite Nombre:')
while nombre!='*':
    gusto=input('Digite el gusto:') #programar
    listaGustos=gustos.setdefault(nombre,[gustos]) #{'Gustavo Hernandez':'musica'}
    if listaGustos!=[gusto]:
        gustos[nombre].append(gusto)
    nombre=input('Digite Nombre:')
print(gustos)



