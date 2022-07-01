def factorial(num): #5
    if num>0:
        valor=num*factorial(num-1)
        print(num)
        return valor
    elif num==0:
        return 1
    else:
        return 1

#METODO PRINCIPAL
if __name__=='__main__':
    numero=int(input('Digite numero:')) #5
    print('Factoria de:', numero,'es', factorial(numero)) #5