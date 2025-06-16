def contador_letras(lista_name):
    nombre_p, nombre_m, nombre_a, nombre_c = 0, 0, 0, 0
    for nombre in lista_name:
        if nombre[0] == 'P' or nombre[0] == 'p':
            nombre_p += 1
        if nombre[0] == 'M' or nombre[0] == 'm':
            nombre_m += 1
        if nombre[0] == 'A' or nombre[0] == 'a':
            nombre_a += 1
        if nombre[0] == 'C' or nombre[0] == 'c':
            nombre_c += 1
    return (nombre_p, nombre_m, nombre_a, nombre_c)


lista_name = ["Pedro", "Manuel", "Maria", "Agustin", "Agustin", "Conrado Puto"]
print(contador_letras(lista_name))