import sys
print('Nota: Debe de ingresar los productos Xn.:')
try:
    Xn = int(input('Ingrese la Xn: '))
    Xn1 = int(input('Ingrese la Xn-1: '))
    corridas = int(input('Ingrese las corridas a generar: '))
    if Xn >= 0000 and Xn <= 9999 & Xn1 >= 0000 and Xn1 <= 9999:
        
        for i in range(corridas):

            
            producto = (Xn+Xn1)%1000
            Xn2 = producto
            print(f'[{i}] producto Xn es: {Xn};  Xn-1:{Xn1};    Xn+Xn-1:{Xn+Xn1}; (Xn+Xn-1)/1000 :{producto};  Xn+1:{Xn2}')
            Xn=Xn2
            Xn1=Xn-1
        print('Programa finalizado.')

    else:
        print('Debe de ingresar digitos, no caracteres.')
except (ValueError):
    print('Tienes un error de tipo: ', sys.exc_info()[0]) 
    print('Nota: Debes introducir valores de tipo numerico.')
