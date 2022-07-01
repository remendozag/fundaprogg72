Funcion operar (num1,num2)
	multiplicacion<-num1*num2
	Escribir multiplicacion
Fin Funcion

Funcion suma <- sumar ( num1,num2 )
	suma<-num1+num2
Fin Funcion

Algoritmo PruebaFuncion
	Definir numero1, numero2 Como Entero
	Escribir 'Digite numero 1:'
	Leer numero1
	Escribir 'Digite numero 1:'
	Leer numero2
	operar(numero1,numero2) //Llamada a la funcion
	Escribir 'La suma es:', sumar(numero1,numero2) //llamar a la funcion con retorno
FinAlgoritmo
