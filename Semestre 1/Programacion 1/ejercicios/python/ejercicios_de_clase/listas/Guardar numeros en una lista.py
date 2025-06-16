print("GUARDAR NUMEROS DENTRO DE UNA LISTA")
print('')
print("Ingrese un numero negativo para salir")
print("=====================================")


def lista_de_num():
    frenar = False
    n_list = []
    while not frenar:
        numero = int(input("Ingrese un numero: "))
        if numero < 0:
            frenar = True
        else:
            n_list.append(numero)
    if not n_list:
        print("La lista de numeros está vacía.")
    for i in n_list:
        if i % 2 != 0:
            n_list.remove(i)
    return n_list


print(lista_de_num())
