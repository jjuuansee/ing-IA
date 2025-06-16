from utilidades import (
    solicitar_input_y_validarlo,
    validar_id,
    validar_nombre_apellido,
    validar_cedula
)
from conexion_bd import verificar_existencia_en_tabla

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------- MODIFICAR ACTIVIDAD CLASE ------------------------------------------------

def modificar_actividad(connection):
    """
    Modifica los detalles de una actividad existente en la base de datos.

    Esta función permite al usuario actualizar la descripción o el costo de una actividad.
    Antes de realizar cambios, valida que la actividad exista, esté activa y no esté siendo utilizada
    por clases actualmente dictadas.

    Flujo de trabajo:
    1. Solicita el ID de la actividad y valida su existencia.
    2. Verifica si la actividad está asociada a clases dictadas actualmente.
       Si lo está, cancela la operación.
    3. Muestra los detalles actuales de la actividad.
    4. Permite al usuario seleccionar el campo a modificar (descripción o costo).
    5. Realiza las actualizaciones en la base de datos y confirma los cambios.

    Parámetros:
    - connection: Conexión activa a la base de datos.

    Retorna:
    - Mensaje de confirmación si la modificación fue exitosa.
    - Mensaje de error o cancelación en caso contrario.
    """

    while True:
        try:
            id_actividad = solicitar_input_y_validarlo(
                "Ingrese el ID de la actividad a modificar (o '0' para cancelar): ",
                lambda x: validar_id(x) or x == "0",
                "ID inválido. Debe ser un número entero positivo."
            )

            if id_actividad == "0":
                return "Operación cancelada."

            if not verificar_existencia_en_tabla(connection, id_actividad, "actividades", "id"):
                print("La actividad no existe o ya está dada de baja.")
                continue

            with connection.cursor() as cursor:
                query_clases_dictadas = """
                    SELECT id
                    FROM clase
                    WHERE id_actividad = %s AND dictada = TRUE AND fecha_de_baja IS NULL
                """
                cursor.execute(query_clases_dictadas, (id_actividad,))
                clases_dictadas = cursor.fetchall()

                if clases_dictadas:
                    clases_ids = [str(clase[0]) for clase in clases_dictadas]
                    print(f"No se puede modificar la actividad porque está siendo utilizada en las clases dictadas "
                          f"con IDs: {', '.join(clases_ids)}.")
                    return "Operación cancelada."


                query_verificar = """
                    SELECT descripcion, costo
                    FROM actividades
                    WHERE id = %s AND fecha_de_baja IS NULL
                """
                cursor.execute(query_verificar, (id_actividad,))
                actividad = cursor.fetchone()

                if not actividad:
                    return "La actividad no existe o ya ha sido dada de baja."

                descripcion_actual, costo_actual = actividad

                while True:
                    print("\nDatos actuales de la actividad:")
                    print(f"1. Descripción: {descripcion_actual}")
                    print(f"2. Costo: {costo_actual} pesos uruguayos")
                    print("0. Cancelar la operación.\n")

                    opcion = input("Seleccione el campo que desea modificar (1-2, o '0' para cancelar): ").strip()

                    if opcion == "0":
                        return "Operación cancelada."

                    elif opcion == "1":  # Modificar descripción
                        nueva_descripcion = solicitar_input_y_validarlo(
                            "Ingrese la nueva descripción: ",
                            validar_nombre_apellido,
                            "Descripción inválida. Debe contener solo letras, espacios o guiones, y tener entre 2 y 50 caracteres."
                        )
                        query_actualizar = "UPDATE actividades SET descripcion = %s WHERE id = %s"
                        cursor.execute(query_actualizar, (nueva_descripcion, id_actividad))

                        # Actualizar descripción en la tabla `equipamiento` si aplica
                        descripcion_equipamiento = f"Kit {nueva_descripcion}"
                        query_actualizar_equipamiento = """
                            UPDATE equipamiento
                            SET descripcion = %s
                            WHERE id_actividad = %s
                        """
                        cursor.execute(query_actualizar_equipamiento, (descripcion_equipamiento, id_actividad))
                        connection.commit()

                        print(f"Descripción actualizada exitosamente: '{descripcion_actual}' -> '{nueva_descripcion}'")
                        descripcion_actual = nueva_descripcion

                    elif opcion == "2":  # Modificar costo
                        nuevo_costo = solicitar_input_y_validarlo(
                            "Ingrese el nuevo costo (mayor a 0): ",
                            lambda x: x.isdigit() and int(x) > 0,
                            "Costo inválido. Debe ser un número entero positivo."
                        )
                        query_actualizar = "UPDATE actividades SET costo = %s WHERE id = %s"
                        cursor.execute(query_actualizar, (nuevo_costo, id_actividad))
                        connection.commit()

                        print(f"Costo actualizado exitosamente: {costo_actual} -> {nuevo_costo}")
                        costo_actual = nuevo_costo

                    else:
                        print("Opción inválida. Por favor seleccione un número válido.")
                        continue

                    # Preguntar si desea modificar otro campo
                    continuar = input("¿Desea modificar otro campo? (Si/No): ").strip().lower()
                    if continuar != "si":
                        return f"Modificación de la actividad con ID {id_actividad} finalizada."

        except Exception as e:
            connection.rollback()
            return f"Error al interactuar con la base de datos: {e}"

# ----------------------------------------------------------------------------------------------------------------------

def modificar_clase(connection):
    """
    Permite modificar los detalles de una clase existente en la base de datos.

    Esta función ofrece al usuario la posibilidad de actualizar tres campos de una clase:
    1. Cédula del instructor asignado.
    2. ID de la actividad asociada.
    3. ID del turno asignado.

    Antes de permitir modificaciones, se realizan las siguientes validaciones:
    - La clase debe existir y no estar dada de baja.
    - La clase no debe estar marcada como dictada (no se pueden modificar clases ya ejecutadas).
    - El nuevo instructor, actividad o turno deben ser válidos y estar activos.

    Flujo de trabajo:
    1. Solicita el ID de la clase y valida su existencia.
    2. Verifica si la clase está activa y no dictada.
    3. Muestra los detalles actuales de la clase.
    4. Permite al usuario seleccionar y modificar un campo específico.
    5. Aplica las modificaciones en la base de datos y confirma los cambios.
    6. Pregunta si desea modificar otro campo o finalizar.

    Parámetros:
    - connection: Conexión activa a la base de datos.

    Retorna:
    - Mensaje de confirmación si las modificaciones son exitosas.
    - Mensaje de error o cancelación en caso contrario.
    """

    try:
        while True:
            id_clase = solicitar_input_y_validarlo(
                "Ingrese el ID de la clase a modificar (o '0' para cancelar): ",
                validar_id,
                "ID inválido. Debe ser un número entero positivo."
            )

            if id_clase == "0":
                return "Operación cancelada."

            with connection.cursor() as cursor:
                query_verificar_clase = """
                    SELECT ci_instructor, id_actividad, id_turno, dictada
                    FROM clase
                    WHERE id = %s AND fecha_de_baja IS NULL
                """
                cursor.execute(query_verificar_clase, (id_clase,))
                clase = cursor.fetchone()

                if not clase:
                    print("La clase no existe o ya ha sido dada de baja.")
                    continue

                ci_instructor_actual, id_actividad_actual, id_turno_actual, dictada = clase

                if dictada:
                    return f"No se puede modificar la clase con ID {id_clase} porque está siendo dictada."

                while True:
                    print("\nDatos actuales de la clase:")
                    print(f"1. CI del instructor: {ci_instructor_actual}")
                    print(f"2. ID de la actividad: {id_actividad_actual}")
                    print(f"3. ID del turno: {id_turno_actual}")
                    print("0. Cancelar la operación.\n")

                    opcion = input("Seleccione el campo que desea modificar (1-3, o '0' para cancelar): ").strip()

                    if opcion == "0":
                        return "Operación cancelada. Volviendo al menú principal."

                    if opcion == "1":  # Modificar CI del instructor
                        nuevo_ci_instructor = solicitar_input_y_validarlo(
                            "Ingrese la nueva cédula del instructor (7-8 dígitos sin puntos ni guiones): ",
                            validar_cedula,
                            "Cédula inválida. Debe contener 7-8 dígitos sin puntos ni guiones."
                        )

                        if not verificar_existencia_en_tabla(connection, nuevo_ci_instructor, "instructores", "ci"):
                            print("El instructor no existe o ya ha sido dado de baja.")
                            continue

                        query_actualizar = "UPDATE clase SET ci_instructor = %s WHERE id = %s"
                        cursor.execute(query_actualizar, (nuevo_ci_instructor, id_clase))
                        connection.commit()
                        print(f"CI del instructor actualizado exitosamente: {ci_instructor_actual} -> {nuevo_ci_instructor}")
                        ci_instructor_actual = nuevo_ci_instructor

                    elif opcion == "2":  # Modificar ID de la actividad
                        nuevo_id_actividad = solicitar_input_y_validarlo(
                            "Ingrese la nueva ID de la actividad: ",
                            validar_id,
                            "ID de actividad inválido. Debe ser un número entero positivo."
                        )

                        if not verificar_existencia_en_tabla(connection, nuevo_id_actividad, "actividades", "id"):
                            print("La actividad no existe o ya ha sido dada de baja.")
                            continue

                        query_actualizar = "UPDATE clase SET id_actividad = %s WHERE id = %s"
                        cursor.execute(query_actualizar, (nuevo_id_actividad, id_clase))
                        connection.commit()
                        print(f"ID de la actividad actualizado exitosamente: {id_actividad_actual} -> {nuevo_id_actividad}")
                        id_actividad_actual = nuevo_id_actividad

                    elif opcion == "3":  # Modificar ID del turno
                        nuevo_id_turno = solicitar_input_y_validarlo(
                            "Ingrese la nueva ID del turno: ",
                            validar_id,
                            "ID de turno inválido. Debe ser un número entero positivo."
                        )

                        if not verificar_existencia_en_tabla(connection, nuevo_id_turno, "turnos", "id"):
                            print("El turno no existe o ya ha sido dado de baja.")
                            continue

                        query_actualizar = "UPDATE clase SET id_turno = %s WHERE id = %s"
                        cursor.execute(query_actualizar, (nuevo_id_turno, id_clase))
                        connection.commit()
                        print(f"ID del turno actualizado exitosamente: {id_turno_actual} -> {nuevo_id_turno}")
                        id_turno_actual = nuevo_id_turno

                    else:
                        print("Opción inválida. Por favor seleccione un número válido.")
                        continue

                    # Preguntar si desea modificar otro campo
                    continuar = input("¿Desea modificar otro campo? (Si/No): ").strip().lower()
                    if continuar not in ["si", "sí"]:
                        return f"Modificaciones completadas para la clase con ID {id_clase}."

    except Exception as e:
        connection.rollback()
        return f"Error al interactuar con la base de datos: {e}"

# ----------------------------------------------------------------------------------------------------------------------
