lista=[1,2,3] #MUTABLE
tupla=(1,2,3) #INMUTABLE
conjunto={1,2,3} #REPITA Y DESORDEN
#CONJUNTOS(SETS)
conjuntoA={5,6,8,9,10}
print(type(conjuntoA))
print(conjuntoA)
conjuntoB={2,4,6,8,10}
print(type(conjuntoB))
print(conjuntoB)
conjuntoA.add(15)
print(conjuntoA)
conjuntoA.remove(9)
print(conjuntoA)
#UNION
union=conjuntoA | conjuntoB
print('La union es:',union)
print(conjuntoA.union(conjuntoB))
#INTERSECCION &
interseccion=conjuntoA & conjuntoB
print('La interseccion es:',interseccion)
print(conjuntoA.intersection(conjuntoB))
#DIFERENCIA -
diferencia=conjuntoA - conjuntoB
print('La diferencia es:',diferencia)
print(conjuntoA.difference(conjuntoB))
diferencia=conjuntoB - conjuntoA
print('La diferencia es:',diferencia)
print(conjuntoB.difference(conjuntoA))
#DIFERENCIA SIMETRICA ^
diferenciaSimetrica=conjuntoA ^ conjuntoB
print('La diferencia simetrica es:',diferenciaSimetrica)
print(conjuntoA.symmetric_difference(conjuntoB))
print(union-interseccion)
#COMPLEMENTO
complemento=union-conjuntoA
print(complemento)



