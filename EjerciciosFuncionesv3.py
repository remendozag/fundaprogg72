def imprimir(menor, mayor): #3, 10
    for menor in range(menor, mayor+1):
        print(menor)


#METODO PRINCIPAL
if __name__=='__main__':
    print('Programa de Funciones')
    menor=int(input('Digite menor:'))
    mayor=int(input('Digite mayor:'))
    imprimir(menor, mayor) #3, 10