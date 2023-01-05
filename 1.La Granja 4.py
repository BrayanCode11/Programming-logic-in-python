'''
4. Al granjero se le dañó el corral y no sabe si volver a cercar el corral con madera, alambre de
puas o poner reja de metal. Si va a cercar con madera debe poner 4 hileras de tablas, con
varilla 8 hileras y con alambre solo 5 hileras, el quiere saber que es lo menos costoso para
cercar si sabe que el alambre de puas vale P por metro, las tablas a Q por metro y las varillas
S por metro. Dado el tama~no del corral y los precios de los elementos, ¿cual cerramiento es
el mas economico?.

'''



def corral_menos_costos(a,b,c,d):

    '''
    Donde:
    a -> Precio de las tablas por metro
    b -> Precio del alambre por metro
    c -> Precio de las varillas por metro
    d -> Metros por hilera
    '''

    corral_madera =  (a*d)*4 

    corral_alambre = (b*d)*5
    
    corral_varilla = (c*d)*8


    if corral_madera < corral_alambre and corral_madera < corral_varilla:
        return "corral de madera" 
         
    elif corral_alambre < corral_madera and corral_alambre < corral_varilla:
        return "corral de alambre"
    
    else:
        return "corral de varilla"
        
def menos_costos_valor(a,b,c,d):

    corral_madera =  (a*d)*4

    corral_alambre = (b*d)*5
    
    corral_varilla = (c*d)*8


    if corral_madera < corral_alambre and corral_madera < corral_varilla:
        return corral_madera
         
    elif corral_alambre < corral_madera and corral_alambre < corral_varilla:
        return corral_alambre
    
    else:
        return corral_varilla

def main():

    tablas=float(input("Digite el valor de un metro de madera: "))

    alambre=float(input("Digite el valor de un metro de alambre: "))

    varilla=float(input("Digite el valor de un metro de varillas: "))

    hileras= float(input("digite los metros por hilera: "))
    
    
    if corral_menos_costos(tablas,alambre,varilla,hileras) == "corral de madera":
        print (corral_menos_costos(tablas,alambre,varilla,hileras),"= ", menos_costos_valor(tablas,alambre,varilla,hileras))
    
    elif corral_menos_costos(tablas,alambre,varilla,hileras) == "corral de alambre":
        print (corral_menos_costos(tablas,alambre,varilla,hileras),"= ", menos_costos_valor(tablas,alambre,varilla,hileras))

    elif corral_menos_costos(tablas,alambre,varilla,hileras) == "corral de varilla":
        print (corral_menos_costos(tablas,alambre,varilla,hileras),"= ", menos_costos_valor(tablas,alambre,varilla,hileras))

main()