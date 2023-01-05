'''
5. Funcion potencia de un entero elevado a un entero.

'''

def fun_potencia (a,b): 
    '''
    Donde:
    a -> Base
    b -> Exponente
    '''

    resultado = a**b

    return resultado

def main():
    
    base = int(input("Digite un numero entero como base a elevar: "))
    exponente = int(input("Digite el exponente a elevar la base: "))

    print("El resultado de elevar" , base , " a la ",exponente, " es = " , fun_potencia(base,exponente))

main()