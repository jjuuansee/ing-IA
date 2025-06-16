print("EDITOR DE TEXTO\n===============")


def corregir_formato(oracion):
    oracion_corregida = ''
    contador = 0
    for letra in oracion:
        if contador == 0 and letra == ' ':
            oracion_corregida += ''
        else:
            oracion_corregida += letra
            contador += 1
    oracion_corregida = oracion_corregida.capitalize()
    return oracion_corregida


def editor_texto():
    seguir_leyendo = True
    simbolos = 0
    espacios = 0
    lista_de_oraciones = []
    while seguir_leyendo:
        oracion = input("Ingrese una oracion que desea agregar a la lista de oraciones: ")
        print("PARA DEJAR DE INGRESAR ORACIONES INGRESE '::q' (dos puntos, dos puntos, letra q) ")
        if oracion == '::q':
            seguir_leyendo = False
        else:
            oracion_corregida = corregir_formato(oracion)
            for letra in oracion_corregida:
                if letra == ' ':
                    espacios += 1
                elif letra in ',.;:¡!¿?()/-_"·$%&*':
                    simbolos += 1
            lista_de_oraciones.append(oracion_corregida)
    return lista_de_oraciones, f"La cantidad de espacios ingresados fueron: {espacios}", f"La cantidad de simbolos ingresados fueron: {simbolos}", f"La cantidad de oraciones ingresadas fueron: {len(lista_de_oraciones)}"

print(editor_texto())