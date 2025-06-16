from conexion_bd import verificar_existencia_en_tabla, validar_clase_no_solapada
from utilidades import (
validar_cedula,
solicitar_input_y_validarlo,
validar_id
)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------- ALUMNO CLASE ---------------------------------------------------

def agregar_alumno_a_clase(connection, ci_usuario, rol):
    """
        Inscribe un alumno a una clase con la opción de asignar un equipamiento.

        Reglas del sistema:
        - Los alumnos solo pueden inscribirse a sí mismos.
        - Los instructores y administradores pueden inscribir a cualquier alumno activo.
        - Se valida que los horarios de la clase no se solapen con otros horarios ya asignados al alumno.
        - Existe la opción de asignar un equipamiento al alumno durante la inscripción.

        Proceso:
        1. Solicita y valida el ID de la clase, asegurándose de que exista y esté activa.
        2. Solicita y valida la cédula del alumno según el rol:
            - 'alumno': Se utiliza la cédula del usuario que inició sesión.
            - 'instructor' o 'administrador': Permite ingresar manualmente la cédula de un alumno.
        3. Verifica que el alumno no esté previamente inscrito en la clase.
        4. Valida que no existan conflictos de horarios con otras clases del alumno.
        5. Pregunta si el alumno necesita un equipamiento:
            - Si es requerido, solicita y valida el ID del equipamiento.
            - Asegura que el equipamiento exista antes de asignarlo.
        6. Registra al alumno en la clase junto con el equipamiento si se proporciona.

        Parámetros:
            - connection: Conexión activa a la base de datos.
            - ci_usuario: Cédula del usuario que realiza la operación.
            - rol: Rol del usuario ('alumno', 'instructor', 'administrador').

        Retorna:
            - Mensaje indicando el éxito de la inscripción o el motivo de la cancelación/error de la operación.

        Notas:
        - Si el alumno no requiere equipamiento, el campo correspondiente en la base de datos se guarda como NULL.
    """
    try:
        with connection.cursor() as cursor:
            while True:
                clase_id = solicitar_input_y_validarlo(
                    "Ingrese el ID de la clase: ",
                    validar_id,
                    "ID inválido. Debe ser un número entero positivo."
                )

                if not verificar_existencia_en_tabla(connection, clase_id, "clase", "id"):
                    print(f"La clase con ID {clase_id} no existe o ha sido dada de baja.")
                    continuar = input("¿Desea intentar con otro ID de clase o cancelar la operación? (Ingrese 'si' para"
                                      " continuar o 'no' para cancelar): ").strip().lower()
                    if continuar not in ['si', 'sí']:
                        return "Operación cancelada."
                    continue
                break

            while True:
                if rol == 'alumno':
                    ci_alumno = ci_usuario
                elif rol in ['instructor', 'administrador']:
                    ci_alumno = solicitar_input_y_validarlo(
                        "Ingrese la cédula del alumno/a a agregar (o '0' para cancelar): ",
                        validar_cedula,
                        "Cédula inválida. Debe contener entre 7 y 8 dígitos numéricos."
                    )
                    if ci_alumno == "0":
                        return "Operación cancelada."
                else:
                    return "Rol no permitido. Operación cancelada."

                if not verificar_existencia_en_tabla(connection, ci_alumno, "alumnos", "ci"):
                    print(f"El alumno con cédula {ci_alumno} no está registrado o ha sido dado de baja.")
                    continuar = input("¿Desea intentar con otra cédula o cancelar la operación? (Ingrese 'si' para continuar o 'no' para cancelar): ").strip().lower()
                    if continuar not in ['si', 'sí']:
                        return "Operación cancelada."
                    continue
                break

            query_verificar_inscripcion = """
                SELECT 1
                FROM alumno_clase
                WHERE id_clase = %s AND ci_alumno = %s
            """
            cursor.execute(query_verificar_inscripcion, (clase_id, ci_alumno))
            if cursor.fetchone():
                return f"El alumno con cédula {ci_alumno} ya está inscrito en la clase {clase_id}."

            if not validar_clase_no_solapada(cursor, clase_id, ci_alumno):
                return f"El alumno con cédula {ci_alumno} tiene un conflicto de horarios con esta clase."

            # Preguntar si se requiere equipamiento
            requiere_equipamiento = input("¿El alumno necesita un equipamiento? (Si/No): ").strip().lower()
            id_equipamiento = None
            if requiere_equipamiento in ['si', 'sí']:
                while True:
                    id_equipamiento = solicitar_input_y_validarlo(
                        "Ingrese el ID del equipamiento: ",
                        validar_id,
                        "ID inválido. Debe ser un número entero positivo."
                    )

                    query_verificar_equipamiento = "SELECT 1 FROM equipamiento WHERE id = %s"
                    cursor.execute(query_verificar_equipamiento, (id_equipamiento,))
                    if cursor.fetchone():
                        break  # ID válido
                    print(f"El ID {id_equipamiento} no corresponde a un equipamiento registrado. Intente nuevamente.")

            # Inscribir al alumno en la clase
            query_inscribir = """
                INSERT INTO alumno_clase (id_clase, ci_alumno, id_equipamiento)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query_inscribir, (clase_id, ci_alumno, id_equipamiento))
            connection.commit()

            mensaje = f"Alumno con cédula {ci_alumno} inscrito exitosamente en la clase {clase_id}."
            if id_equipamiento:
                mensaje += f" Equipamiento asignado: {id_equipamiento}."
            return mensaje

    except Exception as e:
        connection.rollback()
        return f"Error de base de datos: {e}"

# ----------------------------------------------------------------------------------------------------------------------

def eliminar_alumno_de_clase(connection, ci_usuario, rol):
    """
    Permite eliminar a un alumno de una clase específica, cumpliendo las siguientes reglas:
    - Los alumnos solo pueden eliminarse de clases en las que están inscritos.
    - Los instructores y administradores pueden eliminar a cualquier alumno de cualquier clase válida.

    Proceso:
    1. Solicita y valida el ID de la clase, verificando que exista y esté activa.
    2. Solicita y valida la cédula del alumno:
        - 'alumno': Se utiliza la cédula del usuario que inició sesión.
        - 'instructor' o 'administrador': Permite ingresar manualmente la cédula de un alumno.
    3. Verifica que el alumno esté inscrito en la clase indicada.
    4. Si todas las validaciones se cumplen, elimina la inscripción del alumno en la clase.

    Parámetros:
        - connection: Conexión activa a la base de datos.
        - ci_usuario: Cédula del usuario que realiza la operación.
        - rol: Rol del usuario ('alumno', 'instructor', 'administrador').

    Retorna:
        - Mensaje indicando el éxito de la operación o el motivo de su cancelación/error.
    """
    try:
        with connection.cursor() as cursor:
            while True:
                clase_id = solicitar_input_y_validarlo(
                    "Ingrese el ID de la clase (o '0' para cancelar): ",
                    lambda x: validar_id(x) or x == "0",
                    "ID inválido. Debe ser un número entero positivo."
                )
                if clase_id == "0":
                    return "Operación cancelada."


                if not verificar_existencia_en_tabla(connection, clase_id, "clase", "id"):
                    print(f"La clase con ID {clase_id} no existe o ha sido dada de baja.")
                    continuar = input("¿Desea intentar con otro ID de clase o cancelar la operación? (Ingrese 'si' para continuar o 'no' para cancelar): ").strip().lower()
                    if continuar not in ['si', 'sí']:
                        return "Operación cancelada."
                    continue  # Volver a solicitar un nuevo ID de clase
                break  # Si el ID de la clase es válido, salir del bucle


            while True:
                if rol == 'alumno':
                    ci_alumno = ci_usuario  # El alumno solo puede eliminarse a sí mismo
                elif rol in ['instructor', 'administrador']:
                    ci_alumno = solicitar_input_y_validarlo(
                        "Ingrese la cédula del alumno/a a eliminar (o '0' para cancelar): ",
                        lambda x: validar_cedula(x) or x == "0",
                        "Cédula inválida. Debe contener entre 7 y 8 dígitos numéricos."
                    )
                    if ci_alumno == "0":
                        return "Operación cancelada."
                else:
                    return "Rol no permitido."

                # Validar que el alumno exista
                if not verificar_existencia_en_tabla(connection, ci_alumno, "alumnos", "ci"):
                    print(f"El alumno con cédula {ci_alumno} no existe o ha sido dado de baja.")
                    continuar = input("¿Desea intentar con otra cédula o cancelar la operación? (Ingrese 'si' para continuar o 'no' para cancelar): ").strip().lower()
                    if continuar not in ['si', 'sí']:
                        return "Operación cancelada."
                    continue  # Volver a solicitar una nueva cédula

                query_verificar = """
                    SELECT 1
                    FROM alumno_clase
                    WHERE id_clase = %s AND ci_alumno = %s
                """
                cursor.execute(query_verificar, (clase_id, ci_alumno))
                if not cursor.fetchone():
                    print(f"El alumno con cédula {ci_alumno} no está inscrito en la clase {clase_id}.")
                    continuar = input("¿Desea intentar con otra cédula o cancelar la operación? (Ingrese 'si' para continuar o 'no' para cancelar): ").strip().lower()
                    if continuar not in ['si', 'sí']:
                        return "Operación cancelada."
                    continue  # Volver a solicitar una nueva cédula
                break  # Si la cédula es válida y está inscrita, salir del bucle

            query_eliminar = """
                DELETE FROM alumno_clase
                WHERE id_clase = %s AND ci_alumno = %s
            """
            cursor.execute(query_eliminar, (clase_id, ci_alumno))
            connection.commit()

            return f"Alumno con cédula {ci_alumno} eliminado exitosamente de la clase {clase_id}."

    except Exception as e:
        connection.rollback()
        return f"Error de base de datos: {e}"

# ----------------------------------------------------------------------------------------------------------------------
