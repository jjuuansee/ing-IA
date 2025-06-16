print("QUE NUMERO ES MAYOR")
print("===================")


def mayor_de_tres_numeros(n1, n2, n3):
    global es_mayor
    if n1 > n2 and n1 > n3:
        es_mayor = n1
    elif n2 > n1 and n2 > n3:
        es_mayor = n2
    elif n3 > n1 and n3 > n2:
        es_mayor = n3
    elif n1 == n2 == n3:
        print("Los numeros son iguales")
    return es_mayor


n1 = int(input("Ingrese un numero entero: "))
n2 = int(input("Ingrese otro numero entero: "))
n3 = int(input("Ingrese otro numero entero: "))
solucion = mayor_de_tres_numeros(n1, n2, n3)
print("El mayor de los numeros ingresados es:", solucion)

