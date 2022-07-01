'''
from datetime import date,time,datetime
anio=int(input('Digite año:'))
mes=int(input('Digite mes:'))
dia=int(input('Digite dia:'))
fechaNac=date(anio,mes,dia)
print(fecha)
fechaActual=date.today()
resta=fechaActual-fechaNac
print(fecha)
'''

capitales={
    'Chile':'Santiago de Chile',
    'Paraguay':'Asuncion',
    'Uruguay':'Montevideo',
    'Argentina':'Buenos Aires',
    'Brazil':'Brasilia'
}

print(capitales)

for clave, valor in capitales.items():
    print(clave,':',valor)
#METODOS DE DICCIONARIO
print(capitales['Brazil'])
print(capitales['Uruguay'])
del capitales['Paraguay']
print(capitales)
capitales['Colombia']='Santa Fe Bogota'
print(capitales)
print(capitales['Colombia'])
print(capitales.get('Colombia'))
capitales['Colombia']='Bogota DC'
print(capitales)
print(capitales['Colombia'])

#FUNCIONES
def nombreDeLaFuncion(parametros):
    #sentencias
    pass

#METODOS
#capitales.nombreMetodo()
