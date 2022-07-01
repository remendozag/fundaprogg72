#OPERACIONES CON LISTAS
comidasTipicas1=['Ajiaco','Tamal','Changua']
comidasTipicas2=['Bandeja Paisa','Sancocho']
print(comidasTipicas1)
print(comidasTipicas2)
comidas=comidasTipicas1+comidasTipicas2
print(type(comidas))
print(comidas)
comidasTipicas2.append('Bistec')
print(comidasTipicas2)
comidas2=comidasTipicas2*2
print(comidas2)
comidasTipicas2.pop()
print(comidasTipicas2)
comidas.sort()
print(comidas)
comidas.sort(reverse=True)
print(comidas)
comidas.remove('Changua')
print(comidas)

