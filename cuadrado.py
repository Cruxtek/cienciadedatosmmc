import sys

print('Nota: Debe de ingresar 4 digitos en la semilla.')
try:
    semilla = int(input('Ingrese la semilla: '))

    if semilla >= 0000 and semilla <= 9999:

        corridas = int(input('Ingrese las corridas a generar: '))

        for i in range(corridas):

            semilla = semilla
            semilla_alCuadrado = semilla * semilla
            largo_semillaCuadrada = len(str(semilla_alCuadrado))

            if largo_semillaCuadrada == 8:
                s = str(semilla_alCuadrado)
                t = s[2:6]
                v = int(t)
                r = v / 10000
            else:
                if largo_semillaCuadrada != 8:
                    s = str(semilla_alCuadrado)
                    t = s[1:5]
                    v = int(t)
                    r = v / 10000
            print(f'[{i}] La semilla Xo es: {semilla};     Xo²: {semilla_alCuadrado};     Largo: {largo_semillaCuadrada};     Pseudoaleatorio: {v};     Random Ri: {r}')
            semilla = v

            if v == 0:
                print('Límite del Método.')
                break

        print('Programa finalizado.')

    else:
        print('Debe de ingresar  digitos correctos.')
except (ValueError):
    print('Tienes un error de tipo: ', sys.exc_info()[0]) # sys.exc_info() Muestra el tipo de error
    print('Nota: Debes introducir valores de tipo numerico.')
