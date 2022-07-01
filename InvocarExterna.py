#INVOCAR FUNCION EXTERNA
#import FuncionExterna as fe
#print(fe.exponenciar(4,3))
import math #LIBRERIA INTERNA PARA MATEMATICAS
#from math import *
from FuncionExterna import exponenciar
print(exponenciar(4,3)) #LIBRERIA EXTERNA
print(math.pow(4,3))
print(math.pi)
print(math.e)
valorPI=3.141592653589793 #contante
euler=2.718281828459045
print(valorPI)
print(euler)