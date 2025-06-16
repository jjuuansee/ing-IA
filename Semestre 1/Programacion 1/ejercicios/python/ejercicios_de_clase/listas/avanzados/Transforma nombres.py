print("TRANSFORMA NOMBRES\n==================")


def transformar_nombres(lista_de_listas):
    nombres_completos = []
    for nombres, apellidos in lista_de_listas:
        nombre_completo = f"{nombres} {apellidos}"
        nombres_completos.append(nombre_completo)
    return nombres_completos

nombres_apellidos = [ ["Rocky", "Balboa"], ["Muhammad", "Ali"] ]
nombres_completos = transformar_nombres(nombres_apellidos)
print(nombres_completos)
