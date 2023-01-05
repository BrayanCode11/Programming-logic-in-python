'''
1. Si una vaca necesita M metros cuadrados de pasto para producir X litros de leche, ¿cuantos
litros de leche se producen en la granja?.
'''


def cant_leche (a,b,c,d): 
    '''
    Donde: 
    a -> cantidad de vacas que hay en la granja
    b -> área en metros cuadrados con pasto del corral
    c -> Litros de leche que produce una vaca
    d -> metros cuadrados de pasto que necesita una vaca para producir c litros de leche
    
    '''
    

    leche_total = (a*b*c)/d  
    leche_total = round(leche_total , 2)
    
    return leche_total
  
def main():

    vacas = int(input("número de vacas que se crian en la granja: "))

    area_corral_pasto_vacas = float(input ("Digite el area del corral con pasto de la vacas en metros cuadrados: "))

    litros_leche = float(input("Digite los litros de leche por vaca: "))

    pasto_requerido = float(input("Digite el pasto requerido para producir " + str(litros_leche) + " litros de leche por vaca. (En metros cuadrados): "))
   
    print("La leche total que se produce en la granja es= " , cant_leche(vacas,area_corral_pasto_vacas,litros_leche,pasto_requerido), " litros")    

main()    