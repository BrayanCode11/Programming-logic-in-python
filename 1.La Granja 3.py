'''
3. Si los escorpiones de la granja se venden a China, y hay escorpiones de tres diferentes tamaños:
pequeños (con un peso de 20 gramos), medianos (con un peso 30 gramos) y grandes (con 
un peso de 50 gramos), ¿cuantos kilos de escorpiones se pueden vender sin que decrezca la
poblacion a menos de 2/3?.

'''


def poblacion(a,b,c):
    '''
    Donde:
    a -> Cantidad, escorpiones pequeños. 
    b -> Cantidad, escorpiones medianos.
    c -> Cantidad, escorpiones grandes.
    '''

    escorpiones_kilos=((a*20)+(b*30)+(c*50))/1000  #20, 40 y 50 son los pesos en gramos de los escorpiones determinados. 

    poblacion_minima=(escorpiones_kilos)*(2/3)
    
    poblacion_disponible=int(escorpiones_kilos-poblacion_minima)
    
    return poblacion_disponible

def main():


    pequeños=int(input("Ingrese la cantidad de escorpiones pequeños (Con un peso de 20 gramos): "))

    medianos=int(input("Ingrese la cantidad de escorpiones medianos (Con un peso de 30 gramos): "))

    grandes=int(input("Ingrese la cantidad de escorpiones medianos (Con un peso de 50 gramos): "))
    
    print("Se pueden vender ", poblacion(pequeños,medianos,grandes)," kilos de escorpiones a china")

main()