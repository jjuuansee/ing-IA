def recibe_datos():
    piezas_dentales = []
    seguir_leyendo = True
    while seguir_leyendo:
        numero_diente = int(input("Ingrese el numero de la pieza (XX): "))
        print("Para dejar de ingresar el numero de la pieza ingrese (-1): ")
        if 10 <= numero_diente <= 99:
            piezas_dentales.append(numero_diente)
        elif numero_diente == -1:
            seguir_leyendo = False
        else:
            print("Ingrese un numero de pieza valido")
    return piezas_dentales


def dentadura_valida(piezas_dentales):
    rangos_validos = [
        range(11, 18), range(21, 28), range(31, 38), range(41, 48), range(51, 55),
        range(61, 65), range(71, 75), range(81, 85)
    ]
    for numero_diente in piezas_dentales:
        if numero_diente not in rangos_validos:
            return False
        else:
            return True

print (dentadura_valida(recibe_datos()))
