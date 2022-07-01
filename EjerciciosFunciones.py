def intercambiar(num1, num2): #8, 4
    temporal=num2 #4
    num2=num1 #8
    num1=temporal #4
    print('El numero 1:', num1) #4
    print('El numero 2:', num2) #8
    #print('El valor temporal:', temporal) #8


#METODO PRINCIPAL
if __name__=='__main__':
    numero1=int(input('Digite numero 1:')) #8
    numero2=int(input('Digite numero 2:')) #4
    intercambiar(numero1, numero2) #8, 4 INVOCACION FUNCION
