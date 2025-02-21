import sys
print('Nota: Debe de ingresar los productos Xn.:')
try:
    x = int(input('Ingrese la Xn: '))
    a = int(input('Ingrese la cosntante mult: '))
    c = int(input('Ingrese la constante adit: '))
    m = int(input('Ingrese el modulo: '))
    corridas = int(input('Ingrese las corridas a generar: '))
    if x >= 0000 and x <= 9999 :
        
        for i in range(corridas):
            


            print(f'[{i}] producto Xn es: {Xn};     aXn+c:{val}; (aXn+c)/m:{producto};  Xn+1:{Xn1}')
            
            

        print('Programa finalizado.')

    else:
        print('Debe de ingresar digitos, no caracteres.')
except (ValueError):
    print('Tienes un error de tipo: ', sys.exc_info()[0]) 
    print('Nota: Debes introducir valores de tipo numerico.')

