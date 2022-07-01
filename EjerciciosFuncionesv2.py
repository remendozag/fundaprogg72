def mayor(num1,num2,num3):
    if num1>num2 and num2>num3:
        print(num1, num2, num3)
    elif num2>num1 and num2>num3:
        print(num2, num1, num3)
    elif num1>num2 and num3>num2:
        print(num3, num1, num2)
    elif num2>num1 and num3>num2:
        print(num3, num2, num1)
    elif num1<num2 and num3<num2:
        print(num2, num1, num2)
    elif num1==num2 and num2==num3:
        print('Los numeros son iguales')
    else:
        print('Fuera de rango')

#METODO PRINCIPAL
if __name__=='__main__':
    num1=int(input('Digite valor 1:'))
    num2=int(input('Digite valor 2:'))
    num3=int(input('Digite valor 3:'))
    mayor(num1, num2, num3)