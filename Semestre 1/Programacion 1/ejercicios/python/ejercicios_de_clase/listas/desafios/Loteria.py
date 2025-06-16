print("CARTON DE LOTERIA\n=================")

import random


def numero_random():
    return random.randint(1,99)


def generar_carton():
    carton = []
    fila1 = []
    fila2 = []
    fila3 = []
    for i in range(5):
        numero = numero_random()
        if numero not in fila1:
            fila1.append(numero)
    carton.append(fila1)
    for i in range(5):
        numero = numero_random()
        if numero not in carton:
            fila2.append(numero)
    carton.append(fila2)
    for i in range(5):
        numero = numero_random()
        if numero not in carton:
            fila3.append(numero)
    carton.append(fila3)
    return carton

print(generar_carton())