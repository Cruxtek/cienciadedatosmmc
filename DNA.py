import matplotlib.pyplot as plt

def transformar_ADN_ARN(secuencia):
    arn = ""
    for base in secuencia:
        if base == "T":
            arn += "U"
        else:
            arn += base
    return arn


def tieneStartStop(secuencia):
    # Si no tiene el inicio, el final y algo (3 + 3 + algo) entonces no
    if len(secuencia) < 7:
        return False
    inicio = secuencia[:3]
    fin = secuencia[-3:]
    if inicio != "ATG":
        return False
    if fin != "TGA":
        return False
    parte_central = secuencia[3:-3]
    longitud_parte_central = len(parte_central)
    if longitud_parte_central % 3 != 0:
        return False

    if "ATG" in parte_central:
        return False
    if "TGA" in parte_central:
        return False
    # Si pasó todas las validaciones de arriba, entonces es válido
    return True


def mostrar(secuencia):
    longitud = len(secuencia)
    cantidad_a = 0
    cantidad_c = 0
    cantidad_t = 0
    cantidad_g = 0
    for base in secuencia:
        if base == "A":
            cantidad_a += 1
        elif base == "C":
            cantidad_c += 1
        elif base == "T":
            cantidad_t += 1
        elif base == "G":
            cantidad_g += 1

    porcentaje_a = (cantidad_a * 100) / longitud
    porcentaje_c = (cantidad_c * 100) / longitud
    porcentaje_t = (cantidad_t * 100) / longitud
    porcentaje_g = (cantidad_g * 100) / longitud
    salida = ""
    salida += "A " + ("*" * cantidad_a) + " " + str(porcentaje_a) + "% "
    salida += "C " + ("*" * cantidad_c) + " " + str(porcentaje_c) + "% "
    salida += "T " + ("*" * cantidad_t) + " " + str(porcentaje_t) + "% "
    salida += "G " + ("*" * cantidad_g) + " " + str(porcentaje_g) + "% "
    return salida


def resumir(secuencia):
    ultima_base = secuencia[0]
    salida = ""
    conteo = 0
    indice = 0
    for base in secuencia:
        if base == ultima_base:
            conteo += 1
        else:
            if conteo > 0:
                salida += ultima_base + str(conteo)
            conteo = 1
            ultima_base = base

        # Caso especial cuando llegamos al final
        if indice + 1 >= len(secuencia):
            salida += ultima_base + str(conteo)
        indice += 1
    return salida


def duplicar(secuencia):
    salida = ""
    for base in secuencia:
        salida += base*2
    return salida


def segmentos(secuencia):
    print(secuencia)
    conteo = 0
    inicio_de_segmento_encontrado = False
    for base in secuencia:
        if base == "A":
            if inicio_de_segmento_encontrado:
                conteo += 1
                inicio_de_segmento_encontrado = False
        else:
            inicio_de_segmento_encontrado = True
    return conteo




def primeraBaseUnica(secuencia):
    indice = 0
    for base in secuencia:
        # Si la primera ocurrencia de izquierda a derecha (index) es la misma que de derecha a izquierda, entonces
        # esta base solo aparece una vez en la secuencia
        if secuencia.index(base) == secuencia.rindex(base):
            return indice
        indice += 1
    return -1


"""
Realizamos combinaciones de todas las subcadenas. Por ejemplo para AGAG serían las siguientes combinaciones:
A
AG
AGA
AGAG
En cada combinación que hacemos, vemos si al multiplicarla N veces se daría con la cadena completa. N es
las veces que esta subcadena cabe en toda la secuencia, redondeada al entero anterior más próximo. 
Entonces tomando en cuenta cada combinación:
A, al multiplicarla 4 veces da AAAA, no nos da la cadena AGAG entonces lo descartamos
AG, al multiplicarla 2 veces da AGAG, SÍ nos da la cadena AGAG entonces regresamos True y ya no hacemos las siguientes
Otro ejemplo, para AGA:
Para A, multiplicamos por 3. Nos da AAA, no es AGA entonces descartamos
Para AG, multiplicamos por 1, nos da AG, no es AGA entonces descartamos
Para AGA, multiplicamos por 1 y SÍ nos da AGA pero NO lo tomamos en cuneta porque la combinación mide igual que la cadena completa
Llegamos al final de las comprobaciones y regresamos False
"""


def periodica(secuencia):
    longitud_secuencia = len(secuencia)
    for i in range(longitud_secuencia):
        combinacion = secuencia[:i+1]
        longitud_combinacion = len(combinacion)
        cantidad_de_veces_que_cabe = longitud_secuencia // longitud_combinacion
        # Ver si esta subcadena, al multiplicarla por las veces que cabe, es igual a la cadena completa
        # Nota: también comprobamos si la subcadena no es exactamente igual a la cadena original
        multiplicada = combinacion*cantidad_de_veces_que_cabe
        if longitud_combinacion != longitud_secuencia and multiplicada == secuencia:
            return True
    return False


def solicitar_y_validar_secuencia():
    while True:
        secuencia = input("Ingrese la secuencia: ")
        if len(secuencia) < 1:
            print("La longitud de la secuencia debe ser mayor o igual a 1")
            continue
        for base in secuencia:
            correcto = True
            if base.upper() not in "ACTG":
                correcto = False
        if not correcto:
            print("La secuencia solo puede estar conformada por A, C, T o G")
            continue
        # Si ninguno de los "continue" de arriba se cumplió, entonces estamos bien
        # La regresamos en mayúscula porque todas las funciones suponen que estará en mayúscula
        return secuencia.upper()


def menu(secuencia_fija, secuencia):
    while True:
        opcion = input("0. Salir del programa\n1. Transformar\n2. Comprobar si tiene start y stop\n3. Mostrar\n4. Resumir\n5. Duplicar\n6. Expandir\n7. Primera base única\n8. Periódica\nElija: ")
        if opcion == "0":
            return
        # Comprobamos si es necesario solicitar la secuencia
        if not secuencia_fija and opcion != "7":  # opción 7 no necesita secuencia
            secuencia = solicitar_y_validar_secuencia()
        if opcion == "1":
            print(transformar_ADN_ARN(secuencia))
        elif opcion == "2":
            print(tieneStartStop(secuencia))
        elif opcion == "3":
            print(mostrar(secuencia))
        elif opcion == "4":
            print(resumir(secuencia))
        elif opcion == "5":
            print(duplicar(secuencia))
        elif opcion == "6":
            print(segmentos(secuencia))
        elif opcion == "7":
            print(primeraBaseUnica(secuencia))
        elif opcion == "8":
            print(periodica(secuencia))
        else:
            print("Opción inválida")


def main():
    respuesta_secuencia_fija = input(
        "¿Desea trabajar con una secuencia fija? [s/n]: ")
    secuencia = ""
    secuencia_fija = False
    if respuesta_secuencia_fija.lower() == "s":
        secuencia = solicitar_y_validar_secuencia()
        secuencia_fija = True
    menu(secuencia_fija, secuencia)
    plt.secuencia


main()
