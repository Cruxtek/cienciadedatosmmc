import sys
print('Nota: Debe de ingresar los productos Xn.:')
try:
    Xn = int(input('Ingrese la Xn: '))
    
    corridas = int(input('Ingrese las corridas a generar: '))
    if Xn >= 0000 and Xn <= 9999 :
        
        for i in range(corridas):
            
            xmod = 11*Xn
            producto = xmod%32
            Xn1 = producto


            print(f'[{i}] producto Xn es: {Xn};     11Xn:{xmod}; (11Xn)/32:{producto};  Xn+1:{Xn1}')
            
            Xn=Xn1

        print('Programa finalizado.')

    else:
        print('Debe de ingresar digitos, no caracteres.')
except (ValueError):
    print('Tienes un error de tipo: ', sys.exc_info()[0]) 
    print('Nota: Debes introducir valores de tipo numerico.')
