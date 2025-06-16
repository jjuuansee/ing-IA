from conexion_bd import verificar_existencia_en_tabla
from utilidades import (
    validar_cedula,
    validar_nombre_apellido,
    validar_correo,
    validar_contraseña,
    solicitar_input_y_validarlo,
    hash_contraseñas
)
from datetime import datetime

# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------- ABM DE INSTRUCTOR ------------------------------------------------

def alta_instructor(connection):
    """
    Registra un nuevo instructor en la base de datos.
    Valida y solicita los datos del instructor: cédula, nombre, apellido, correo y contraseña,
    asegurándose de que no existan registros duplicados.

    Flujo:
    1. Valida la cédula ingresada, verificando que no esté registrada previamente.
    2. Solicita y valida el nombre y apellido.
    3. Solicita y valida un correo único para el instructor.
    4. Solicita y valida una contraseña con al menos 6 caracteres.
    5. Registra los datos en las tablas `login` e `instructores`.

    Permite cancelar el proceso en cualquier momento.
    Retorna un mensaje indicando el resultado del registro.
    """

    datos_instructor = {}

    try:
        with connection.cursor() as cursor:
            while True:
                if "ci" in datos_instructor:
                    print(f"Cédula actual: {datos_instructor['ci']}")
                cedula_instructor = input("Ingresa la cédula del nuevo/a instructor/ra (o '0' para salir): ")
                if not validar_cedula(cedula_instructor):
                    print("Cédula inválida. Debe contener exactamente 7 u 8 dígitos sin puntos ni guiones.")
                    continue

                if cedula_instructor == "0":
                    return "Operación cancelada."
                if verificar_existencia_en_tabla(connection, cedula_instructor, "instructores", "ci"):
                    print(f"La cédula {cedula_instructor} ya está registrada como instructor/ra.")
                    respuesta = input("¿Desea volver atrás? (Ingrese 0 para salir, o cualquier otra cosa para continuar): ")
                    if respuesta == "0":
                        return "Has salido del registro de instructores."
                    continue
                datos_instructor["ci"] = cedula_instructor
                break

            datos_instructor["nombre"] = solicitar_input_y_validarlo(
                "Ingresa el nombre del nuevo/a instructor/ra: ",
                validar_nombre_apellido,
                "El nombre solo debe contener letras, y tener una cantidad de 2 a 50 caracteres."
            )

            datos_instructor["apellido"] = solicitar_input_y_validarlo(
                "Ingresa el apellido del nuevo/a instructor/ra: ",
                validar_nombre_apellido,
                "El apellido solo debe contener letras y tener un máximo de 50 caracteres."
            )

            while "correo" not in datos_instructor:
                correo = input("Ingresa el correo del nuevo/a instructor/ra: ")
                if not validar_correo(correo):
                    print("Correo inválido. Intente nuevamente.")
                    continue
                if verificar_existencia_en_tabla(connection, correo, "login", "correo"):
                    print(f"El correo {correo} ya está registrado. Intente con otro correo.")
                    continue
                datos_instructor["correo"] = correo

            datos_instructor["contraseña"] = solicitar_input_y_validarlo(
                "Ingresa la contraseña del nuevo/a instructor/ra (mínimo 6 caracteres): ",
                validar_contraseña,
                "Contraseña inválida. Debe tener al menos 6 caracteres."
            )
            datos_instructor["contraseña"] = hash_contraseñas(datos_instructor["contraseña"])

            # Insertar credenciales en la tabla `login`
            query_login = "INSERT INTO login (correo, contraseña, rol) VALUES (%s, %s, 'instructor')"
            cursor.execute(query_login, (datos_instructor["correo"], datos_instructor["contraseña"]))

            # Obtener el ID generado en la tabla `login`
            id_login = cursor.lastrowid

            # Insertar instructor en la tabla `instructores`
            query_instructor = "INSERT INTO instructores (ci, nombre, apellido, id_login) VALUES (%s, %s, %s, %s)"
            cursor.execute(query_instructor, (
                datos_instructor["ci"],
                datos_instructor["nombre"],
                datos_instructor["apellido"],
                id_login
            ))

            connection.commit()
            return f"Instructor/a registrado exitosamente: {datos_instructor['nombre']} {datos_instructor['apellido']}."

    except Exception as e:
        connection.rollback()
        return f"Error al registrar el instructor: {e}"

# ----------------------------------------------------------------------------------------------------------------------

def baja_instructor(connection):
    """
    Permite dar de baja a un instructor verificando previamente su existencia y que no esté asociado a clases dictadas.

    Flujo:
    1. Solicita la cédula del instructor y valida su formato.
    2. Permite cancelar la operación ingresando '0'.
    3. Verifica si el instructor existe y está activo en la base de datos.
    4. Verifica si el instructor está asociado a clases dictadas activas:
       - Si está asociado, informa al usuario y cancela la operación.
    5. Muestra los datos del instructor encontrado y solicita confirmación para darlo de baja.
    6. Actualiza las fechas de baja en las tablas `instructores` y `login`.
    7. Retorna un mensaje indicando el éxito o el motivo de la cancelación.

    En caso de error con la base de datos, revierte los cambios y retorna un mensaje de error.
    """

    while True:
        try:
            cedula_instructor = solicitar_input_y_validarlo(
                "Ingrese la cédula del instructor/a a dar de baja (7-8 dígitos sin puntos ni guiones, o '0' para cancelar): ",
                validar_cedula,
                "Cédula inválida. Asegúrese de ingresar 7-8 dígitos sin puntos ni guiones."
            )

            if cedula_instructor == "0":
                return "Operación cancelada."

            if not verificar_existencia_en_tabla(connection, cedula_instructor, "instructores", "ci"):
                print("El instructor/a no existe o ya ha sido dado/a de baja.")
                continue

            with connection.cursor() as cursor:
                query_clases_dictadas = """
                    SELECT c.id
                    FROM clase c
                    WHERE c.ci_instructor = %s AND c.dictada = 1 AND c.fecha_de_baja IS NULL
                """
                cursor.execute(query_clases_dictadas, (cedula_instructor,))
                clases_dictadas = cursor.fetchall()

                if clases_dictadas:
                    # Informar al usuario sobre las clases dictadas
                    ids_clases = [str(clase['id']) for clase in clases_dictadas]
                    return f"No se puede dar de baja al instructor porque está asignado a clases actualmente dictadas con IDs: {', '.join(ids_clases)}."

                # Verificar si el instructor tiene datos asociados
                query_verificar_instructor = """
                    SELECT i.nombre, i.apellido, l.correo
                    FROM instructores i
                    JOIN login l ON i.id_login = l.id
                    WHERE i.ci = %s AND i.fecha_de_baja IS NULL
                """
                cursor.execute(query_verificar_instructor, (cedula_instructor,))
                resultado = cursor.fetchone()

                if not resultado:
                    return "El instructor/a no existe o ya ha sido dado/a de baja."

                nombre, apellido, correo = resultado

                print(f"Instructor/a encontrado/a: {nombre} {apellido}")

                confirmar = input(f"¿Está seguro/a de que desea dar de baja a {nombre} {apellido}? (Sí/No): ").strip().lower()
                if confirmar not in ['si', 'sí']:
                    return "Operación cancelada. Volviendo al menú principal."

                # Actualizar fecha de baja en `instructores` y `login`
                fecha_baja = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                query_baja_instructor = "UPDATE instructores SET fecha_de_baja = %s WHERE ci = %s"
                query_baja_login = "UPDATE login SET fecha_de_baja = %s WHERE correo = %s"

                cursor.execute(query_baja_instructor, (fecha_baja, cedula_instructor))
                cursor.execute(query_baja_login, (fecha_baja, correo))

                connection.commit()

                return f"Instructor/a {nombre} {apellido} dado/a de baja exitosamente."

        except Exception as e:
            connection.rollback()
            return f"Error al interactuar con la base de datos: {e}"

# ----------------------------------------------------------------------------------------------------------------------

def modificar_instructor(connection):
    """
    Permite modificar los datos de un instructor registrado en el sistema. Los campos que pueden modificarse son:
    nombre, apellido y correo electrónico.

    Flujo:
    1. Solicita la cédula del instructor y valida su formato.
    2. Permite cancelar la operación ingresando '0'.
    3. Verifica si el instructor existe y está activo en la base de datos.
    4. Obtiene y muestra los datos actuales del instructor.
    5. Solicita al usuario seleccionar el campo que desea modificar:
       - Modificar el nombre: valida que contenga solo letras y tenga entre 2 y 50 caracteres.
       - Modificar el apellido: valida que contenga solo letras y tenga entre 2 y 50 caracteres.
       - Modificar el correo: valida el formato del correo y verifica que no esté registrado previamente.
    6. Realiza la actualización en la base de datos y confirma los cambios.
    7. Permite modificar múltiples campos antes de finalizar o cancelar la operación.

    En caso de error con la base de datos, revierte los cambios y retorna un mensaje de error.
    """

    while True:
        try:
            cedula_instructor = solicitar_input_y_validarlo(
                "Ingrese la cédula del instructor/a a modificar (o '0' para "
                "cancelar): ",
                validar_cedula,
                'Cédula inválida. Asegúrese de ingresar entre 7 y 8 dígitos numéricos en el rango permitido.'
            )

            if cedula_instructor == "0":
                return "Operación cancelada."

            if not verificar_existencia_en_tabla(connection, cedula_instructor, "instructores", "ci"):
                print(f"El instructor con cédula {cedula_instructor} no existe o ya está dado de baja.")
                continue

            with connection.cursor() as cursor:
                query_obtener_instructor = """
                    SELECT i.nombre, i.apellido, l.correo, l.id 
                    FROM instructores i
                    JOIN login l ON i.id_login = l.id
                    WHERE i.ci = %s AND i.fecha_de_baja IS NULL
                """
                cursor.execute(query_obtener_instructor, (cedula_instructor,))
                instructor = cursor.fetchone()

                if not instructor:
                    print(f"No se encontraron datos activos para el instructor con cédula {cedula_instructor}.")
                    continue

                nombre_actual, apellido_actual, correo_actual, id_login = instructor

                while True:
                    print(f"\nDatos actuales del instructor:")
                    print(f"1. Nombre: {nombre_actual}")
                    print(f"2. Apellido: {apellido_actual}")
                    print(f"3. Correo: {correo_actual}")
                    print("0. Cancelar la operación.")

                    opcion = input("\nSeleccione el campo que desea modificar (1-3, o '0' para cancelar): ").strip()

                    if opcion == "0":
                        return "Operación cancelada."

                    elif opcion == "1":  # Modificar nombre
                        nuevo_nombre = solicitar_input_y_validarlo(
                            'Ingrese el nuevo nombre: ',
                            validar_nombre_apellido,
                            'Nombre inválido. Debe contener solo letras y tener entre 2 y 50 caracteres.'
                        )
                        query_actualizar_nombre = "UPDATE instructores SET nombre = %s WHERE ci = %s"
                        cursor.execute(query_actualizar_nombre, (nuevo_nombre, cedula_instructor))
                        connection.commit()
                        print(f"Nombre actualizado exitosamente: {nombre_actual} -> {nuevo_nombre}")
                        nombre_actual = nuevo_nombre  # Actualizar para reflejar los cambios
                        continue

                    elif opcion == "2":  # Modificar apellido
                        nuevo_apellido = solicitar_input_y_validarlo(
                            'Ingrese el nuevo apellido: ',
                            validar_nombre_apellido,
                            'Apellido inválido. Debe contener solo letras y tener entre 2 y 50 caracteres.'
                        )
                        query_actualizar_apellido = "UPDATE instructores SET apellido = %s WHERE ci = %s"
                        cursor.execute(query_actualizar_apellido, (nuevo_apellido, cedula_instructor))
                        connection.commit()
                        print(f"Apellido actualizado exitosamente: {apellido_actual} -> {nuevo_apellido}")
                        apellido_actual = nuevo_apellido  # Actualizar para reflejar los cambios
                        continue

                    elif opcion == "3":  # Modificar correo
                        while True:
                            nuevo_correo = solicitar_input_y_validarlo(
                                'Ingrese el nuevo correo: ',
                                validar_correo,
                                'Correo inválido. Asegúrese de ingresar un correo en formato válido (@ucu.edu.uy o @correo.ucu.edu.uy).'
                            )
                            # Verificar si el correo ya está registrado en `login`
                            if verificar_existencia_en_tabla(connection, nuevo_correo, "login", "correo"):
                                print("El correo ya está registrado en el sistema. Intente con otro.")
                                continue
                            break

                        query_actualizar_correo = "UPDATE login SET correo = %s WHERE id = %s"
                        cursor.execute(query_actualizar_correo, (nuevo_correo, id_login))
                        connection.commit()
                        print(f"Correo actualizado exitosamente: {correo_actual} -> {nuevo_correo}")
                        correo_actual = nuevo_correo  # Actualizar para reflejar los cambios
                        continue

                    else:
                        print("Opción inválida. Por favor seleccione un número válido.")
                        continue

        except Exception as e:
            connection.rollback()
            return f"Error al interactuar con la base de datos: {e}"
# ----------------------------------------------------------------------------------------------------------------------
