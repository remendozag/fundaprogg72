lista_elementos=[1,2,3,4,5,6]
print(lista_elementos)
listaC=[elemento for elemento in lista_elementos if elemento%2==0]
print(listaC)
conjunto_elementos={1,2,3,4,5,6}
print(conjunto_elementos)
conjuntoC={elemento for elemento in conjunto_elementos if elemento%2!=0}
print(conjuntoC)