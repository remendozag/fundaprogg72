#DICCIONARIOS
mi_diccionario={}
print(type(mi_diccionario))
print(mi_diccionario)
concesionarioMercedesBenz={
    #'key':'value',
    'marca':'Mercedes Benz',
    'modelo':'A4',
    'año':2023
}
print(type(concesionarioMercedesBenz))
print(concesionarioMercedesBenz)
#METODOS
print(concesionarioMercedesBenz.values())
print(concesionarioMercedesBenz.keys())
print(concesionarioMercedesBenz.items())
#CONCESIONARIO CON FOR EACH
for iterador in concesionarioMercedesBenz:
    print(iterador,':',concesionarioMercedesBenz[iterador])

#FOR VALUES
for iterador in concesionarioMercedesBenz.values():
    print(iterador)

#FOR KEYS
for iterador in concesionarioMercedesBenz.keys():
    print(iterador)

#FOR ITEMS
for clave, valor in concesionarioMercedesBenz.items():
    print(clave,':',valor)

