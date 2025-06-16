from utilidades import (
    validar_hora,
    validar_id,
    solicitar_input_y_validarlo
)
from datetime import datetime, timedelta

# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- ABM DE TURNOS -----------------------------------------------------

def alta_turnos(connection):
    """
    Registra un nuevo turno en la base de datos, asegurando que:
    - Los horarios de inicio y fin estén en formato HH:MM y dentro del rango permitido (07:00 a 23:00).
    - La duración del turno esté entre 1 y 4 horas.
    - No exista un turno duplicado con los mismos horarios.

    Procedimiento:
    1. Solicita y valida los horarios de inicio y fin del turno.
    2. Calcula la duración del turno y verifica que cumpla con los límites establecidos.
    3. Comprueba si los horarios ya están registrados como un turno activo en la base de datos.
    4. Si todas las validaciones pasan, inserta el nuevo turno en la tabla `turnos`.

    Parámetros:
        - connection: Conexión activa a la base de datos.

    Retorna:
        - Un mensaje de éxito con los horarios del turno registrado.
        - Un mensaje de error en caso de problemas con la base de datos.
    """
    try:
        while True:
            hora_inicio = solicitar_input_y_validarlo(
                "Ingrese el horario de inicio del turno (HH:MM): ",
                validar_hora,
                "Horario inválido. Asegúrese de usar el formato HH:MM entre 07:00 y 23:00."
            )

            hora_fin = solicitar_input_y_validarlo(
                "Ingrese el horario de finalización del turno (HH:MM): ",
                validar_hora,
                "Horario inválido. Asegúrese de usar el formato HH:MM entre 07:00 y 23:00."
            )

            hora_inicio_dt = datetime.strptime(hora_inicio, '%H:%M')
            hora_fin_dt = datetime.strptime(hora_fin, '%H:%M')

            if hora_fin_dt <= hora_inicio_dt:
                print("Horario inválido. La hora de finalización debe ser mayor que la hora de inicio.")
                continue

            duracion = hora_fin_dt - hora_inicio_dt
            if not (timedelta(hours=1) <= duracion <= timedelta(hours=4)):
                print("Horario inválido. La duración del turno debe estar entre 1 y 4 horas.")
                continue

            with connection.cursor() as cursor:
                query_verificar_duplicado = """
                    SELECT 1
                    FROM turnos
                    WHERE hora_inicio = %s AND hora_fin = %s AND fecha_de_baja IS NULL
                """
                cursor.execute(query_verificar_duplicado, (hora_inicio, hora_fin))
                if cursor.fetchone():
                    print("El turno ya existe en la base de datos. Por favor, ingrese un horario diferente.")
                    continue

            # Si todas las validaciones pasan, salir del bucle
            break

        # Insertar el turno en la base de datos
        with connection.cursor() as cursor:
            query_insertar_turno = "INSERT INTO turnos (hora_inicio, hora_fin) VALUES (%s, %s)"
            cursor.execute(query_insertar_turno, (hora_inicio, hora_fin))
            connection.commit()

        return f"Turno registrado exitosamente: {hora_inicio} - {hora_fin}."

    except Exception as e:
        connection.rollback()
        return f"Error al interactuar con la base de datos: {e}"

# ----------------------------------------------------------------------------------------------------------------------

def baja_turnos(connection):
    """
    Permite dar de baja un turno en la base de datos, asegurándose de que:
    - El turno existe y está activo.
    - El turno no esté asociado con clases activas.

    Procedimiento:
    1. Solicita y valida el ID del turno.
    2. Verifica que el turno exista y no haya sido previamente dado de baja.
    3. Comprueba si el turno está asociado con clases activas. Si lo está, no permite la operación.
    4. Solicita confirmación al usuario para proceder con la baja.
    5. Si se confirma, actualiza la fecha de baja del turno en la base de datos.

    Parámetros:
        - connection: Conexión activa a la base de datos.

    Retorna:
        - Un mensaje de éxito si el turno fue dado de baja correctamente.
        - Un mensaje indicando el motivo en caso de que la operación no pueda completarse.
        - Un mensaje de error si ocurre algún problema al interactuar con la base de datos.
    """
    while True:
        try:
            id_turno = solicitar_input_y_validarlo(
                "Ingrese el ID del turno a dar de baja (o '0' para cancelar): ",
                lambda x: validar_id(x) or x == "0",
                "ID inválido. Debe ser un número entero positivo."
            )

            if id_turno == "0":
                return "Operación cancelada."

            id_turno = int(id_turno)

            with connection.cursor() as cursor:
                query_verificar = "SELECT hora_inicio, hora_fin FROM turnos WHERE id = %s AND fecha_de_baja IS NULL"
                cursor.execute(query_verificar, (id_turno,))
                turno = cursor.fetchone()

                if not turno:
                    print("El turno no existe o ya está dado de baja.")
                    continue

                hora_inicio, hora_fin = turno
                print(f"Turno encontrado:\n- ID: {id_turno}\n- Horario: {hora_inicio} - {hora_fin}")

                query_clases_asociadas = """
                    SELECT id
                    FROM clase
                    WHERE id_turno = %s AND fecha_de_baja IS NULL
                """
                cursor.execute(query_clases_asociadas, (id_turno,))
                clases_asociadas = cursor.fetchall()

                if clases_asociadas:
                    # Extraer los IDs de las clases asociadas
                    ids_clases = [str(clase[0]) for clase in clases_asociadas]
                    return f"No se ha podido dar de baja el turno debido a clases activas con IDs: {', '.join(ids_clases)}"

                # Confirmar la baja con el usuario
                confirmar = input(f"¿Está seguro/a de que desea dar de baja el turno con ID {id_turno}? (Si/No): ").strip().lower()
                if confirmar not in ['si', 'sí']:
                    return "Operación cancelada. Volviendo al menú principal."

                # Dar de baja el turno
                query_baja_turno = "UPDATE turnos SET fecha_de_baja = NOW() WHERE id = %s"
                cursor.execute(query_baja_turno, (id_turno,))

                connection.commit()

                return f"Turno con ID {id_turno} dado de baja exitosamente."

        except Exception as e:
            connection.rollback()
            return f"Error al interactuar con la base de datos: {e}"

# ----------------------------------------------------------------------------------------------------------------------

def modificar_turnos(connection):
    """
    Permite modificar los horarios de un turno existente en la base de datos, asegurando que:
    - El turno existe y no ha sido dado de baja.
    - Los nuevos horarios sean válidos y cumplan con los requisitos establecidos.
    - No haya conflictos con otros turnos existentes.
    - El turno no esté asociado a clases que ya hayan sido dictadas.

    Procedimiento:
    1. Solicita el ID del turno y valida su existencia y estado.
    2. Verifica si el turno está siendo utilizado por clases que ya han sido dictadas.
       Si es así, cancela la operación.
    3. Solicita y valida los nuevos horarios de inicio y fin, asegurando que:
       - Estén en el formato HH:MM.
       - Cumplan con el rango horario permitido (07:00 a 23:00).
       - La duración del turno esté entre 1 y 4 horas.
    4. Comprueba que los nuevos horarios no coincidan con otro turno existente.
    5. Si todas las validaciones son exitosas, actualiza los horarios del turno en la base de datos.

    Parámetros:
        - connection: Conexión activa a la base de datos.

    Retorna:
        - Un mensaje de éxito si el turno se actualizó correctamente.
        - Un mensaje indicando el motivo si la operación no pudo completarse.
        - Un mensaje de error si ocurre algún problema al interactuar con la base de datos.
    """
    while True:
        try:
            id_turno = solicitar_input_y_validarlo(
                "Ingrese el ID del turno a modificar (o '0' para cancelar): ",
                lambda x: validar_id(x) or x == "0",
                "ID inválido. Debe ser un número entero positivo."
            )

            if id_turno == "0":
                return "Operación cancelada."

            id_turno = int(id_turno)

            with connection.cursor() as cursor:
                query_verificar = "SELECT hora_inicio, hora_fin FROM turnos WHERE id = %s AND fecha_de_baja IS NULL"
                cursor.execute(query_verificar, (id_turno,))
                turno_actual = cursor.fetchone()

                if not turno_actual:
                    print("El turno no existe o ya está dado de baja.")
                    continue

                hora_inicio_actual, hora_fin_actual = turno_actual
                print(f"Horario actual del turno: {hora_inicio_actual} - {hora_fin_actual}")

                query_clases_dictadas = """
                    SELECT id
                    FROM clase
                    WHERE id_turno = %s AND dictada = 1
                """
                cursor.execute(query_clases_dictadas, (id_turno,))
                clases_dictadas = cursor.fetchall()

                if clases_dictadas:
                    # Extraer los IDs de las clases dictadas
                    ids_clases = [str(clase[0]) for clase in clases_dictadas]
                    return f"No se puede modificar el turno porque está siendo utilizado en clases dictadas con IDs: {', '.join(ids_clases)}"

                nuevo_hora_inicio = solicitar_input_y_validarlo(
                    "Ingrese el nuevo horario de inicio (HH:MM): ",
                    validar_hora,
                    "Horario inválido. Asegúrese de usar el formato HH:MM entre 07:00 y 23:00."
                )

                nuevo_hora_fin = solicitar_input_y_validarlo(
                    "Ingrese el nuevo horario de finalización (HH:MM): ",
                    validar_hora,
                    "Horario inválido. Asegúrese de usar el formato HH:MM entre 07:00 y 23:00."
                )

                duracion = datetime.strptime(nuevo_hora_fin, '%H:%M') - datetime.strptime(nuevo_hora_inicio, '%H:%M')
                if not (timedelta(hours=1) <= duracion <= timedelta(hours=4)):
                    print("Horario inválido. La duración del turno debe estar entre 1 y 4 horas.")
                    continue

                query_verificar_duplicado = """
                    SELECT 1
                    FROM turnos
                    WHERE hora_inicio = %s AND hora_fin = %s AND id != %s AND fecha_de_baja IS NULL
                """
                cursor.execute(query_verificar_duplicado, (nuevo_hora_inicio, nuevo_hora_fin, id_turno))
                if cursor.fetchone():
                    print("El nuevo horario ya existe en otro turno. Intente con un horario diferente.")
                    continue

                # Actualizar el turno en la base de datos
                query_actualizar_turno = """
                    UPDATE turnos
                    SET hora_inicio = %s, hora_fin = %s
                    WHERE id = %s
                """
                cursor.execute(query_actualizar_turno, (nuevo_hora_inicio, nuevo_hora_fin, id_turno))
                connection.commit()

                return f"Turno con ID {id_turno} actualizado exitosamente: {nuevo_hora_inicio} - {nuevo_hora_fin}."

        except Exception as e:
            connection.rollback()
            return f"Error al interactuar con la base de datos: {e}"

# ----------------------------------------------------------------------------------------------------------------------
