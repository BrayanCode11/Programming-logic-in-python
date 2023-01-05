'''
6. Una funcion que determine si un numero es divisible por otro.

'''

def num_divisible(x,y):
    
    if x%y == 0:
        return True
    
    else:
        return False
        
def main():

    a = float(input("Digite un numero: "))
    b = float(input("Digite un numero para saber si " + str(a) + " es divisible por este: "))

    if num_divisible(a,b) == True:
        print("El numero " + str(a) + " es divisible por " , b)

    else:
        print("El numero " + str(a) + " no es divisible por " , b)         

main()