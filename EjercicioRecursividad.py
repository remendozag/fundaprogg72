'''
Implemente un algoritmo, usando una función recursiva, que resuelva la siguiente sumatoria:
K(n, p) = p + 2 * p + 3 * p + 4 * p + … + n * p
● El programa debe pedir al usuario que ingrese un número n, y un número p,
● Luego debe calcular el valor de K(n, p) usando una función recursiva,
● Debe imprimir el resultado de K(n, p)
'''
def sumatoriaK(n,p, sumatoria): #5,2
    while n>0:
        sumatoria+=n*p
        n-=1
        sumatoriaK(n,p,sumatoria)
    return sumatoria


#METODO PRINCIPAL
if __name__=='__main__':
    n=int(input('Digite numero n:')) #5
    p=int(input('Digite numero p:')) #2
    sumatoria=0
    print(sumatoriaK(n,p,sumatoria)) #5,2

    '''
    valor=5
    conta5=0
    conta6=0
    if valor==5:
        conta5+=1 #conta5=conta5+1
    elif valor==6:
        conta6+=1 #conta5=conta5+1
    print(conta5)
    contaPares=0
    contaImpares=0
    while True:
        numero=int(input('Digite numero:'))
        if numero%2==0:
            print('numero es par')
            contaPares+=1
        else:
            print('numero es impar')
            contaImpares+=1
        if numero==9999:
            break
    print(contaPares)
    print(contaImpares)
    '''
