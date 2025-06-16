print("LISTA CON 10 NUMEROS RANDOM")
print("===========================")


import random
lista_con_diez = []
for i in range(10):
    num = random.randint(1,10)
    lista_con_diez.append(num)
print("Lista de valores:", lista_con_diez)
for elemento in lista_con_diez:
    cuadrado = elemento ** 2
    cubo = elemento ** 3
    print(f"Elemento: {elemento}, Cuadrado: {cuadrado}, Cubo: {cubo}")
