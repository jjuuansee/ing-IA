print("POLINOMIO DE SEGUNDO GRADO")
print("==========================")

import math


def calcular_raices(a, b, c):
    discriminante = b ** 2 - 4 * a * c
    raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
    return raiz1, raiz2


a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
raiz1, raiz2 = calcular_raices(a, b, c)
print(f"Raíz 1: {raiz1}")
print(f"Raíz 2: {raiz2}")
