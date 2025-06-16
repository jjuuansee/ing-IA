print("FORMATEAR NOMBRE")
print("================")


def formatearnombre(nombre, apellido, cedula):
    resultado = f"{apellido}, {nombre} tiene el numero de cedula {cedula}"
    return resultado


nombre_ej = input("Ingrese su nombre: ")
apellido_ej = input("Ingrese su apellido: ")
cedula_ej = input("Ingrese su cedula: ")
print(formatearnombre(nombre_ej, apellido_ej, cedula_ej))
