#SINTAXIS FUNCIONES
def nombreFuncionVacia():
    #FUNCION VACIA
    pass

'''
def nombreFuncion():
    #FUNCION IMPRESION
    print('Salida de la Funcion')
'''
def restar(num1, num2): # 7, 5
    resta=num1-num2 #2
    print('La resta es:', resta) #2
'''
def nombreFuncionConRetorno(parametros):
    #FUNCION CON RETORNO
    return 'Salida de la Funcion'
'''
def sumar(num1, num2): #7, 5
    suma=num1+num2 #12
    return suma #12
#INVOCACION DE FUNCIONES
numero1=float(input('Digite numero 1:')) #7
numero2=float(input('Digite numero 2:')) #5
print('La suma es:', sumar(numero1, numero2)) #12
restar(numero1, numero2) #2



