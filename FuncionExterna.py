#FUNCION EXTERNA
def exponenciar(base, exponente):
    return base**exponente

#METODO PRINCIPAL
if __name__=='__main__':
    #INVOCACION DE LA FUNCION CON RETORNO
    base=float(input('Digite base:'))
    exponente=int(input('Digite exponente:'))
    print(exponenciar(base,exponente)) #64
