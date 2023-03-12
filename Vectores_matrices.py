import libreria_complejos as lc
import math


def sumaVector(v1, v2):
    """
    La función suma de vectores recibe dos vectores de números complejos
    (listas de longitud n que a su vez tienen listas de longitud 2), donde
    se suma posición por posición en el vector y a su vez componente a componente,
    es decir parte real con real e imaginaria con imaginaria
    """
    res = []
    if len(v1) == len(v2):
        for i in range(len(v1)):
            res.append(lc.suma(v1[i][0], v2[i][0]))
        return res
    else:
        return "Syntax Error"


def restaVector(v1, v2):
    """
    La función resta de vectores recibe dos vectores de números complejos
    (listas de longitud n que a su vez tienen listas de longitud 2), donde
    se resta posición por posición en el vector y a su vez componente a componente,
    es decir parte real con real e imaginaria con imaginaria
    """
    res = []
    if len(v1) == len(v2):
        for i in range(len(v1)):
            res.append(lc.resta(v1[i][0], v2[i][0]))
        return res
    else:
        return "Syntax Error"


def inversoAditivoVector(v1):
    """
    La función inverso aditivo de un vector complejo recibe una lista de
    longitud n que a su vez contienen listas de longitud 2 y devuelve cada
    posición del vector multiplicada por el complejo [-1,0]
    """
    res = []
    for i in range(len(v1)):
        res.append(lc.producto(v1[i][0], [-1, 0]))
    return res


def productoEscalarVector(v1, ec1):
    """
    La función producto de un escalar por un vector complejo recibe un escalar
    (lista de longitud 2) y un vector (listas de longitud n que a su vez tienen
    listas de longitud 2) y devuelve la operación de multiplicar el escalar por
    cada elemento del vector
    """
    res = []
    for i in range(len(v1)):
        for j in range(len(v1[0])):
            res.append(lc.producto(v1[i][0], ec1))
    return res


def adicionMatrices(m1, m2):
    """
    La función adición de matrices complejas recibe dos matrices (lista de longitud
    n que contiene una lista de longitud n y que a su vez contiene complejos, es decir
    listas de longitud 2) y devuelve la suma de cada posición [i][j] de cada matriz,
    para esta operación se requiere que las matrices sean de mismo tamaño
    """
    res = []
    if len(m1) == len(m2):
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                res.append(lc.suma(m1[i][j], m2[i][j]))
        return res
    else:
        return "Syntax Error"


def inversoAditivoMatriz(m1):
    """
    La función inversa aditiva de una matriz recibe una matriz (lista de
    longitud n que contiene una lista de longitud n y que a su vez contiene complejos,
    es decir listas de longitud 2) y devuelve cada posición de la matriz multiplicada
    por el complejo [-1,0]
    """
    res = []
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res.append(lc.producto(m1[i][j], [-1, 0]))
    return res


def productoEscalarMatriz(m1, ec1):
    """
    La función producto de un escalar por una matriz complejo recibe un escalar
    (lista de longitud 2) y una matriz (listas de longitud n que contienen listas
    de longitud n y a su vez tienen listas de longitud 2) y devuelve la operación
    de multiplicar el escalar por cada elemento del vector
    """
    res = []
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res.append(lc.producto(m1[i][j], ec1))
    return res


def transpuestaMV(m1):
    """
    La función transpuesta de una matriz recibe una matriz de numeros complejos
    recibe una matriz (listas de longitud n que contienen listas de longitud n y
    a su vez tienen listas de longitud 2) y devuelve la matriz con sus filas y
    columnas cambiadas
    """
    filas = len(m1)
    columnas = len(m1[0])
    m2 = [[None for i in range(filas)] for j in range(columnas)]

    for i in range(filas):
        for j in range(columnas):
            m2[j][i] = m1[i][j]
    return m2


def conjugadoMV(m1):
    """
    La función conjugado recibe una matriz (listas de longitud n que contienen listas
    de longitud n y a su vez tienen listas de longitud 2) y devuelve el conjugado de
    cada elemento de la matriz
    """
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] = lc.conjugado(m1[i][j])
    return m1


def dagaMV(m1):
    """
    La función daga recibe una matriz (listas de longitud n que contienen listas
    de longitud n y a su vez tienen listas de longitud 2) y devuelve la operación daga,
    es decir la transpuesta de la conjugada
    """
    return transpuestaMV(conjugadoMV(m1))


def productoMatrices(m1, m2):
    """
    la función producto de matrices recibe dos matrices de números complejos y retorna
    la operación de multiplicar las matrices, para esto se requiere que el número de
    columnas de la primera matriz sea igual al número de filas de la segunda, y se opera
    multiplicando filas de la primera matriz con las columnas de la segunda matriz
    """
    filasm1, filasm2 = len(m1), len(m2)
    columnasm1, columnasm2 = len(m1[0]), len(m2[0])
    if columnasm1 == filasm2:
        mr = [[[0, 0] for columnas in range(columnasm2)] for filas in range(filasm1)]
        for i in range(filasm1):
            for j in range(columnasm2):
                for k in range(filasm2):
                    mr[i][j] = lc.suma(mr[i][j], lc.producto(m1[i][k], m2[k][j]))
        return mr
    else:
        return "Syntax Error"


def accion(m1, v2):
    """
    La función acción recibe una matriz y un vector, donde retorna la operación de
    multiplicar la matriz poer el vector, de forma que se cumpla la condición de
    la multiplicación de matrices
    """
    return productoMatrices(m1, v2)


def productoInterno(v1, v2):
    """
    La función producto interno recibe dos vectores y retorna la  multiplicación de
    la daga del primer vector con el segundo vector
    """
    return productoMatrices(dagaMV(v1), v2)


def normaV(v1):
    """
    la funcion norma recibe un solo vector, y retorna como resultado la raíz
    cuadrada de la operación del producto interno entre el mismo vector
    """
    x = productoInterno(v1, v1)
    complejo = [x[0][0][0], x[0][0][1]]
    return lc.modulo(complejo)


def distanciaVectores(v1, v2):
    """
    La función distancia entre vectores recibe dos vectores y retorna la
    operación de la norma de la difetencia entre el vector 2 y el 1
    """
    resta = restaVector(v1, v2)
    res = normaV(resta)
    return res


def unitaria(m1):
    """
    la función unitaria recibe una matriz y retorna un booleano: True si al multiplicar
    la matriz con su daga, es igual a la matriz identidad
    """
    filas = len(m1)
    columnas = len(m1[0])
    mIdentidad = [[1 if j == i else 0 for j in range(columnas)] for i in range(filas)]

    if productoMatrices(m1, dagaMV(m1)) == mIdentidad:
        return True
    else:
        return False


def hermitiana(m1):
    """
    La función hermitiana recibe una matriz y retorna un booleano: True si la
    matriz es igual a su daga
    """
    if dagaMV(m1) == m1:
        return True
    else:
        return False


def productoTensorial(m1, m2):
    """
    La función producto tensorial recibe dos matrices y como resultado
    devuelve la operación de hacer producto tensorial entre las dos matrices
    """
    filasm1, filasm2 = len(m1), len(m2)
    columnasm1, columnasm2 = len(m1[0]), len(m2[0])
    mr = [[[0, 0] for i in range(columnasm1 * columnasm2)] for j in range(filasm1 * filasm2)]
    for i in range(len(mr)):
        for j in range(len(mr[0])):
            mr[i][j] = lc.producto(m1[i // filasm2][j // columnasm2], m2[i % filasm2][j % columnasm2])
    return mr
