Funcion quicksort ( L, principio, final )
    i<-principio
    j<-final
    pivote<-(L[i]+L[j])/2
    Mientras i<j Hacer
        Mientras L[i]<pivote Hacer
            i<-i+1
        Fin Mientras
        Mientras L[j]>pivote Hacer
            j<-j-1
        Fin Mientras
        Si i<=j Entonces
            temporal<-L[i]
            L[i]<-L[j]
            L[j]<-temporal
            i<-i+1
            j<-j-1
        Fin Si
    Fin Mientras
    Si principio<j Entonces
        quicksort(L,principio,j)
    Fin Si
    Si final>i Entonces
        quicksort(L,i,final)
    Fin Si
Fin Funcion
Algoritmo ordenar
    Dimension numeros[10]
    // Genero un arreglo de 10 nmeros aleatorios
    Para i<-1 Hasta 10 Con Paso 1 Hacer
        numeros[i] <- azar(100)+1
    Fin Para
    Escribir "Desordenados..."
    Para i<-1 Hasta 10 Con Paso 1 Hacer
        Escribir numeros[i]
    Fin Para
    quicksort(numeros,1,10)
    // Como se pasa por REFERENCIA, numeros se modificara dentro de la funcion
    Escribir "Ordenados..."    
    Para i<-1 Hasta 10 Con Paso 1 Hacer
        Escribir numeros[i]
    Fin Para
FinAlgoritmo