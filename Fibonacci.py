def fibonacci(numero):
    if numero==0:
        return 0
    if numero==1:
        return 1
    return fibonacci(numero-1)+fibonacci(numero-2)


def imprimirSerie(numero):
    fibonacciVector=[]
    for conta_i in range(0, numero+1):
        fibonacciVector.append(fibonacci(conta_i))
        #print('Fibonacci en', conta_i,'es',fibonacci(conta_i))
    return fibonacciVector


#METODO PRINCIPAL
if __name__=='__main__':
    numero=int(input('Digite numero de la serie:'))
    print(fibonacci(numero)) #2
    print(imprimirSerie(numero))
    #[0,1,1,2,3,5,8....]