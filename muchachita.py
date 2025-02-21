import sys
print('Nota: Debe de ingresar los productos Xn.:')
try:
    Xn = int(input('Ingrese la Xn: '))
    a = int(input('Ingrese la cosntante mult: '))
    c = int(input('Ingrese la constante adit: '))
    m = int(input('Ingrese el modulo: '))
    corridas = int(input('Ingrese las corridas a generar: '))
    if Xn >= 0000 and Xn <= 9999 :
        
        for i in range(corridas):
            
            val = a*Xn+c
            producto = val%m**31
            Xn1 = producto-1


            print(f'[{i}] producto Xn es: {Xn};     aXn+c:{val}; (aXn+c)/m:{producto};  Xn+1:{Xn1}')
            
            Xn=Xn1

            u=x/m
            if u == 0.05:
                
        print('Programa finalizado.')

    else:
        print('Debe de ingresar digitos, no caracteres.')
except (ValueError):
    print('Tienes un error de tipo: ', sys.exc_info()[0]) 
    print('Nota: Debes introducir valores de tipo numerico.')

