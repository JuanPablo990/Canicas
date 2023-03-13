# Juan Pablo Nieto Cortes

import math

def suma(c1, c2):
    return [c1[0] + c2[0], c1[1] + c2[1]]


def resta(c1, c2):
    return [c1[0] - c2[0], c1[1] - c2[1]]


def producto(c1, c2):
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imaginario = c1[0] * c2[1] + c1[1] * c2[0]
    return [real, imaginario]


def division(c1, c2):
    num = producto(c1, conjugado(c2))
    denomi = producto(c2, conjugado(c2))
    real = num[0] / denomi[0]
    imaginario = num[1] / denomi[0]
    return [real, imaginario]


def conjugado(c1):
    return [c1[0], c1[1]*-1]


def modulo(c1):

    return math.sqrt(c1[0]**2 + c1[1]**2)


def imprimir(c1):
    if c1[1] > 0:
        return str(c1[0])+'+'+str(c1[1]) + 'i'
    else:
        return str(c1[0])+str(c1[1]) + 'i'


def cart_pol(c1):
    r = math.sqrt(c1[0]**2 + c1[1]**2)
    angle = math.degrees(math.atan2(c1[1], c1[0]))
    return [r, angle]


def pol_cart(c1):
    r, angle = c1[0], math.radians(c1[1])
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    return [x, y]


def fase(c1):
    return math.degrees(math.atan2(c1[1], c1[0]))


def imprimir_exponencial(c1):
    return str(modulo(c1))+"e^i"+" ("+str(fase(c1))+")"

def potencia_n(c1,n):
    if n>1:
        rta = 0

        for i in range(1,n+1):
            if i == 1:
                rta = c1
            else:
                rta = producto(rta,c1)
        return rta
    elif n == 1:
        return c1
