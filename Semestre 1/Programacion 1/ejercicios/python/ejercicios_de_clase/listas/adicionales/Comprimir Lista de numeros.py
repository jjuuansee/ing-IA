def comprimir_lista_num(lista_num):
    lista_comprimida = []
    for num in lista_num:
        if num not in lista_comprimida:
            lista_aux = [num]
            cantidad = lista_num.count(num)
            if cantidad > 1:
                lista_aux.append(cantidad)
            if lista_aux not in lista_comprimida:
                lista_comprimida.append(lista_aux)
    return lista_comprimida


print(comprimir_lista_num([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))