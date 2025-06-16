print("DIFERENCIA SIMETRICA DE DOS LISTAS\n==================================")


def diferencia_simetrica(lista1, lista2):
    lista_simetrica = []
    for i in lista1:
        if i not in lista_simetrica:
            lista_simetrica.append(i)
    for i in lista2:
        if i not in lista_simetrica:
            lista_simetrica.append(i)
        else:
            lista_simetrica.remove(i)
    return lista_simetrica


seguir_leyendo = True
lista1 = []
lista2 = []
print("INGRESE LOS ELEMENTOS DE LA LISTA\n\nPARA SALIR INGRESE 0\n====================")
while seguir_leyendo:
    item = int(input("Ingrese un elemento para agregar a la lista 1: "))
    if item == 0:
        seguir_leyendo = False
    else:
        lista1.append(item)
seguir_leyendo = True
while seguir_leyendo:
    item = int(input("Ingrese un elemento para agregar a la lista 2: "))
    if item == 0:
        seguir_leyendo = False
    else:
        lista2.append(item)

print(diferencia_simetrica(lista1, lista2))


