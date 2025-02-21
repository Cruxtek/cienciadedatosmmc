import sys
print('Nota: Debe de ingresar los productos Xn, Xn-1.:')
try:
    Xn = int(input('Ingrese la Xn: '))
    Xn1 = int(input('Ingrese la Xn-1: '))
    corridas = int(input('Ingrese las corridas a generar: '))
    if Xn >= 0000 and Xn <= 9999 & Xn1 >= 0000 and Xn1 <= 9999 :
        
        for i in range(corridas):
            Xn = Xn1
            producto = Xn * Xn1
            largo_producto = len(str(producto))

            if largo_producto == 8:
                s = str(producto)
                t = s[2:6]
                v = int(t)
                r = v / 10000
            else:
                if largo_producto != 8:
                    s = str(producto)
                    t = s[1:5]
                    v = int(t)
                    r = v / 10000
            print(f'[{i}] producto Xn es: {Xn};     Xn-1:{Xn1}; (Xn)*(Xn-1): {producto};     Largo: {largo_producto};     Pseudoaleatorio: {v};     Aleatorio: {r}')
            Xn1 = v
            
            if v == 0 :
                print('Límite del Método.')
                break

        print('Programa finalizado.')

    else:
        print('Debe de ingresar digitos, no caracteres.')
except (ValueError):
    print('Tienes un error de tipo: ', sys.exc_info()[0]) # sys.exc_info() Muestra el tipo de error
    print('Nota: Debes introducir valores de tipo numerico.')
