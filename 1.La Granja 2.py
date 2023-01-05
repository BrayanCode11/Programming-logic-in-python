'''
2. Si 1/3 de las aves que hay en la granja son gallinas, y la mitad de las gallinas ponen 1 huevo
cada 3 dias y la otra mitad 1 huevo cada 5 dias, en un mes ¿cuantos huevos producen?
(1 mes = 30 dias).'''


def cant_huevos(x): # x -> Cantidad total de aves en la granja

    gallinas = int(x / 3)  #Cantidad de gallinas de la granja

    primera_mitad_huevos = int((30 / 3) * int(gallinas / 2)) #Huevos producidos; Gallinas que ponen 1 cada 3 días.
    
    segunda_mitad_huevos = int((30 / 5) * int(gallinas / 2)) #Huevos producidos; Gallinas que ponen 1 cada 5 días.
    
    total_huevos_mes = primera_mitad_huevos + segunda_mitad_huevos
    
    return total_huevos_mes

def main():
    aves_Total = int(input("número de aves que se crian en la granja: "))
    print("los huevos producidos al mes son=", cant_huevos(aves))

main()    

