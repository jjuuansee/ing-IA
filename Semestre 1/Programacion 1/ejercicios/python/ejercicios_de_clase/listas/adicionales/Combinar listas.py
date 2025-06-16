def combinar_lista(lista1, lista2):
    global lista_mayor
    lista_combinada = []
    if len(lista1) == len(lista2):
        lista_menor = lista1
    elif len(lista1) > len(lista2):
        lista_menor = lista2
        lista_mayor = lista1
    else:
        lista_menor = lista1
        lista_mayor = lista2
    for i in range(len(lista_menor)):
        lista_combinada.append(lista1[i])
        lista_combinada.append(lista2[i])

    lista_combinada = lista_combinada + (lista_mayor[len(lista_mayor) - len(lista_menor) + 1 :])
    return lista_combinada


print(combinar_lista([1, 2, 3], ["a", "b", "c", "d", "e"]))
