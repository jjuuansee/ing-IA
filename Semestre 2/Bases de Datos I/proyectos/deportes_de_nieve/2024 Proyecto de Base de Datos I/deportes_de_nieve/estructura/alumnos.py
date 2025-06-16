from conexion_bd import verificar_existencia_en_tabla
from utilidades import (
    validar_cedula,
    validar_nombre_apellido,
    validar_correo,
    validar_contraseña,
    validar_fecha_nacimiento,
    validar_telefono,
    solicitar_input_y_validarlo,
    hash_contraseñas
)
from datetime import datetime

# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------- ABM DE ALUMNO ----------------------------------------------------

def alta_alumno(connection):
    """
    Registra un nuevo alumno en la base de datos después de realizar varias validaciones:

    1. Valida y solicita los siguientes datos del alumno:
        - Cédula: Se asegura que no esté duplicada en las tablas `alumnos` o `instructores`.
        - Nombre y Apellido: Solo letras, espacios o guiones, con un máximo de 50 caracteres.
        - Fecha de nacimiento: Formato `yyyy-mm-dd` y que el alumno sea mayor de 18 años.
        - Teléfono: Debe contener exactamente 9 dígitos y comenzar con "09".
        - Correo: Se valida que pertenezca a los dominios permitidos y no esté registrado.
        - Contraseña: Mínimo 6 caracteres, se guarda encriptada.

    2. Permite reintentar la entrada de datos en caso de errores de validación para evitar frustraciones del usuario.

    3. Realiza dos inserciones en la base de datos:
        - Primero, crea un registro en la tabla `login` para almacenar las credenciales del alumno.
        - Luego, utiliza el ID generado para insertar los datos en la tabla `alumnos`.

    4. Si ocurre un error durante la transacción, revierte todos los cambios realizados.

    Retorna:
        - Mensaje de éxito con los datos registrados si la operación es completada.
        - Mensaje de error en caso de fallo al interactuar con la base de datos.
    """

    alumno_data = {}

    while True:
        try:
            with connection.cursor() as cursor:
                if "cedula" not in alumno_data:
                    alumno_data["cedula"] = solicitar_input_y_validarlo(
                        "Ingrese la cédula del alumno/a (o '0' para cancelar): ",
                        validar_cedula,
                        "Cédula inválida. Debe contener exactamente 7-8 dígitos numéricos dentro del rango permitido."
                    )

                    if alumno_data["cedula"] == "0":
                        return "Operación cancelada."

                    if verificar_existencia_en_tabla(connection, alumno_data["cedula"], "alumnos", "ci"):
                        print("La cédula ya está registrada como estudiante. Intente con otra.")
                        del alumno_data["cedula"]  # Eliminar la cédula para forzar el reingreso
                        continue

                    if verificar_existencia_en_tabla(connection, alumno_data["cedula"], "instructores", "ci"):
                        print("La cédula ya está registrada como instructor. No puede ser registrada como alumno.")
                        del alumno_data["cedula"]  # Eliminar la cédula para forzar el reingreso
                        continue

                if "nombre" not in alumno_data:
                    alumno_data["nombre"] = solicitar_input_y_validarlo(
                        "Ingrese el nombre del alumno/a: ",
                        validar_nombre_apellido,
                        "Nombre inválido. Debe contener solo letras y un máximo de 50 caracteres."
                    )

                if "apellido" not in alumno_data:
                    alumno_data["apellido"] = solicitar_input_y_validarlo(
                        "Ingrese el apellido del alumno/a: ",
                        validar_nombre_apellido,
                        "Apellido inválido. Debe contener solo letras y un máximo de 50 caracteres."
                    )

                if "fecha_nacimiento" not in alumno_data:
                    alumno_data["fecha_nacimiento"] = solicitar_input_y_validarlo(
                        "Ingrese la fecha de nacimiento del alumno/a (formato yyyy-mm-dd): ",
                        validar_fecha_nacimiento,
                        "Fecha de nacimiento inválida. Debe estar en formato yyyy-mm-dd y ser mayor de 18 años."
                    )

                if "telefono" not in alumno_data:
                    alumno_data["telefono"] = solicitar_input_y_validarlo(
                        "Ingrese el teléfono del alumno/a (9 dígitos): ",
                        validar_telefono,
                        "Teléfono inválido. Debe contener exactamente 9 dígitos numéricos y comenzar con 09."
                    )

                if "correo" not in alumno_data:
                    alumno_data["correo"] = solicitar_input_y_validarlo(
                        "Ingrese el correo del alumno/a: ",
                        validar_correo,
                        "Correo inválido. Debe ser válido y pertenecer a los dominios permitidos."
                    )

                    if verificar_existencia_en_tabla(connection, alumno_data["correo"], "login", "correo"):
                        print("El correo ya está registrado como estudiante. Intente con otro correo.")
                        del alumno_data["correo"]  # Eliminar el correo para forzar el reingreso
                        continue

                if "contraseña" not in alumno_data:
                    alumno_data["contraseña"] = solicitar_input_y_validarlo(
                        "Ingrese la contraseña del alumno/a (mínimo 6 caracteres): ",
                        validar_contraseña,
                        "Contraseña inválida. Debe tener al menos 6 caracteres."
                    )
                    alumno_data["contraseña"] = hash_contraseñas(alumno_data["contraseña"])

                query_login = """
                    INSERT INTO login (correo, contraseña, rol)
                    VALUES (%s, %s, 'alumno')
                """
                cursor.execute(query_login, (alumno_data["correo"], alumno_data["contraseña"]))

                # Obtener el ID del login recién insertado
                id_login = cursor.lastrowid

                # Insertar en tabla `alumnos`
                query_alumno = """
                    INSERT INTO alumnos (ci, nombre, apellido, fecha_nacimiento, telefono, id_login)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_alumno, (
                    alumno_data["cedula"], alumno_data["nombre"], alumno_data["apellido"],
                    alumno_data["fecha_nacimiento"], alumno_data["telefono"], id_login
                ))

                connection.commit()
                return f"""
                Registro exitoso:
                - Nombre: {alumno_data["nombre"]}
                - Apellido: {alumno_data["apellido"]}
                - Cédula: {alumno_data["cedula"]}
                - Correo: {alumno_data["correo"]}
                """

        except Exception as e:
            connection.rollback()
            return  f"Error al interactuar con la base de datos: {e}"

# ----------------------------------------------------------------------------------------------------------------------

def baja_alumno(connection):
    """
    Permite dar de baja a un alumno en el sistema, marcándolo como inactivo en la base de datos.

    Proceso:
    1. Solicita la cédula del alumno a dar de baja:
        - Valida que sea una cédula correcta (7-8 dígitos).
        - Permite cancelar la operación ingresando "0".
    2. Verifica si el alumno existe y está activo en el sistema:
        - Busca en la tabla `alumnos` un registro con la cédula proporcionada que no tenga una fecha de baja.
        - Si no encuentra el alumno, solicita otra cédula.
    3. Extrae los datos del alumno (nombre, apellido, correo) y los muestra al usuario.
    4. Solicita confirmación para proceder con la baja:
        - Si el usuario no confirma, cancela la operación.
    5. Marca al alumno como inactivo:
        - Actualiza la fecha de baja en las tablas `alumnos` y `login`.
        - Utiliza la fecha y hora actual del sistema.
    6. Confirma la transacción si todo se realiza correctamente.
    7. Maneja cualquier error que ocurra durante la transacción, revirtiendo los cambios si es necesario.

    Retorna:
        - Un mensaje de éxito con el nombre y apellido del alumno si la operación se completa.
        - Un mensaje de error si ocurre algún problema durante la interacción con la base de datos.
    """

    while True:
        try:
            cedula_alumno = solicitar_input_y_validarlo(
                "Ingrese la cédula del alumno/a a dar de baja (o '0' para cancelar): ",
                validar_cedula,
                "Cédula inválida. Asegúrese de ingresar 7-8 dígitos sin puntos ni guiones."
            )

            if cedula_alumno == "0":
                return "Operación cancelada."

            with connection.cursor() as cursor:
                query_verificar_alumno = """
                    SELECT a.nombre, a.apellido, l.correo 
                    FROM alumnos a
                    JOIN login l ON a.id_login = l.id
                    WHERE a.ci = %s AND a.fecha_de_baja IS NULL
                """
                cursor.execute(query_verificar_alumno, (cedula_alumno,))
                resultado = cursor.fetchone()

                if not resultado:
                    print("El alumno/a no existe o ya está dado/a de baja.")
                    continue

                nombre, apellido, correo_alumno = resultado
                print(f"Alumno/a encontrado: {nombre} {apellido}")

                confirmar = input(f"¿Está seguro/a de que desea dar de baja a {nombre} {apellido}? (Si/No): ").strip().lower()
                if confirmar not in ['si', 'sí']:
                    return "Operación cancelada. Volviendo al menú principal."

                fecha_baja = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                query_baja_alumno = "UPDATE alumnos SET fecha_de_baja = %s WHERE ci = %s"
                query_baja_login = "UPDATE login SET fecha_de_baja = %s WHERE correo = %s"

                cursor.execute(query_baja_alumno, (fecha_baja, cedula_alumno))
                cursor.execute(query_baja_login, (fecha_baja, correo_alumno))

                connection.commit()
                return f"Alumno/a {nombre} {apellido} dado/a de baja exitosamente."

        except Exception as e:
            connection.rollback()
            return f"Error al interactuar con la base de datos: {e}"

# ----------------------------------------------------------------------------------------------------------------------

def modificar_alumno(connection):
    """
    Permite modificar los datos de un alumno registrado en el sistema.

    Proceso:
    1. Solicita la cédula del alumno que se desea modificar:
        - Valida que sea una cédula correcta (7-8 dígitos numéricos).
        - Permite cancelar la operación ingresando "0".
    2. Verifica si el alumno existe y está activo:
        - Busca al alumno en la tabla `alumnos` con una cédula válida y sin fecha de baja.
        - Si no se encuentra el registro, solicita otra cédula.
    3. Muestra los datos actuales del alumno:
        - Nombre, apellido, correo, fecha de nacimiento y teléfono.
    4. Permite seleccionar el campo que se desea modificar:
        - **Nombre**: Acepta solo letras, espacios y guiones, con longitud entre 2 y 50 caracteres.
        - **Apellido**: Mismas validaciones que el nombre.
        - **Correo**: Acepta correos válidos pertenecientes a dominios permitidos y que no estén registrados.
        - **Fecha de nacimiento**: Verifica formato válido (yyyy-mm-dd) y que el alumno sea mayor de 18 años.
        - **Teléfono**: Debe contener exactamente 9 dígitos y comenzar con "09".
    5. Realiza la actualización en la base de datos:
        - Se ejecuta la consulta SQL correspondiente para el campo seleccionado.
        - Si la modificación es exitosa, actualiza el valor localmente y muestra un mensaje de confirmación.
    6. Permite modificar múltiples campos del mismo alumno:
        - Después de cada modificación, pregunta si se desea continuar.
    7. Maneja errores durante la transacción:
        - Si ocurre algún problema, revierte los cambios realizados.

    Retorna:
        - Un mensaje de éxito por cada campo modificado.
        - Un mensaje de error si ocurre algún problema durante la interacción con la base de datos.
    """

    while True:
        try:
            # Solicitar cédula del alumno con validación
            cedula_alumno = solicitar_input_y_validarlo(
                "Ingrese la cédula del alumno/a a modificar (o '0' para cancelar): ",
                validar_cedula,
                "Cédula inválida. Debe contener exactamente 7-8 dígitos numéricos dentro del rango permitido."
            )

            # Permitir al usuario cancelar la operación
            if cedula_alumno == "0":
                return "Operación cancelada."

            # Verificar si el alumno existe y está activo
            with connection.cursor() as cursor:
                query_verificar_alumno = """
                    SELECT a.nombre, a.apellido, l.correo, a.fecha_nacimiento, a.telefono, l.id
                    FROM alumnos a
                    JOIN login l ON a.id_login = l.id
                    WHERE a.ci = %s AND a.fecha_de_baja IS NULL
                """
                cursor.execute(query_verificar_alumno, (cedula_alumno,))
                resultado = cursor.fetchone()

                if not resultado:
                    print("El alumno/a no existe o ya está dado/a de baja.")
                    continue

                # Extraer datos del alumno
                nombre_actual, apellido_actual, correo_actual, fecha_nacimiento_actual, telefono_actual, id_login = resultado

                # Loop para modificar múltiples campos si se desea
                while True:
                    # Mostrar los datos actuales del alumno
                    print("\nDatos actuales del alumno/a:")
                    print(f"1. Nombre: {nombre_actual}")
                    print(f"2. Apellido: {apellido_actual}")
                    print(f"3. Correo: {correo_actual}")
                    print(f"4. Fecha de nacimiento: {fecha_nacimiento_actual}")
                    print(f"5. Teléfono: {telefono_actual}")
                    print("0. Cancelar la operación.\n")

                    # Solicitar qué campo desea modificar
                    opcion = input("Seleccione el campo que desea modificar (1-5, o '0' para cancelar): ").strip()

                    if opcion == "0":
                        return "Operación cancelada. Volviendo al menú principal."

                    elif opcion == "1":  # Modificar nombre
                        nuevo_nombre = solicitar_input_y_validarlo(
                            'Ingrese el nuevo nombre: ',
                            validar_nombre_apellido,
                            'Nombre inválido. Debe contener solo letras y un máximo de 50 caracteres.'
                        )
                        query_actualizar = "UPDATE alumnos SET nombre = %s WHERE ci = %s"
                        cursor.execute(query_actualizar, (nuevo_nombre, cedula_alumno))
                        connection.commit()
                        print(f"Nombre actualizado exitosamente: {nombre_actual} -> {nuevo_nombre}")
                        nombre_actual = nuevo_nombre

                    elif opcion == "2":  # Modificar apellido
                        nuevo_apellido = solicitar_input_y_validarlo(
                            'Ingrese el nuevo apellido: ',
                            validar_nombre_apellido,
                            'Apellido inválido. Debe contener solo letras y un máximo de 50 caracteres.'
                        )
                        query_actualizar = "UPDATE alumnos SET apellido = %s WHERE ci = %s"
                        cursor.execute(query_actualizar, (nuevo_apellido, cedula_alumno))
                        connection.commit()
                        print(f"Apellido actualizado exitosamente: {apellido_actual} -> {nuevo_apellido}")
                        apellido_actual = nuevo_apellido

                    elif opcion == "3":  # Modificar correo
                        nuevo_correo = solicitar_input_y_validarlo(
                            'Ingrese el nuevo correo: ',
                            lambda correo: validar_correo(correo) and not verificar_existencia_en_tabla(
                                connection, correo, "login", "correo"),
                            'Correo inválido o ya registrado. Por favor, ingrese un correo válido y único.'
                        )
                        # Actualizar el correo en la tabla `login`
                        query_actualizar_login = "UPDATE login SET correo = %s WHERE id = %s"
                        cursor.execute(query_actualizar_login, (nuevo_correo, id_login))
                        connection.commit()
                        print(f"Correo actualizado exitosamente: {correo_actual} -> {nuevo_correo}")
                        correo_actual = nuevo_correo

                    elif opcion == "4":  # Modificar fecha de nacimiento
                        nueva_fecha_nacimiento = solicitar_input_y_validarlo(
                            'Ingrese la nueva fecha de nacimiento (yyyy-mm-dd): ',
                            validar_fecha_nacimiento,
                            'Fecha de nacimiento inválida. Asegúrese de usar el formato yyyy-mm-dd.'
                        )
                        query_actualizar = "UPDATE alumnos SET fecha_nacimiento = %s WHERE ci = %s"
                        cursor.execute(query_actualizar, (nueva_fecha_nacimiento, cedula_alumno))
                        connection.commit()
                        print(f"Fecha de nacimiento actualizada exitosamente: {fecha_nacimiento_actual} -> {nueva_fecha_nacimiento}")
                        fecha_nacimiento_actual = nueva_fecha_nacimiento

                    elif opcion == "5":  # Modificar teléfono
                        nuevo_telefono = solicitar_input_y_validarlo(
                            'Ingrese el nuevo teléfono (9 dígitos): ',
                            validar_telefono,
                            'Teléfono inválido. Debe contener exactamente 9 dígitos y comenzar con 09.'
                        )
                        query_actualizar = "UPDATE alumnos SET telefono = %s WHERE ci = %s"
                        cursor.execute(query_actualizar, (nuevo_telefono, cedula_alumno))
                        connection.commit()
                        print(f"Teléfono actualizado exitosamente: {telefono_actual} -> {nuevo_telefono}")
                        telefono_actual = nuevo_telefono

                    else:
                        print("Opción inválida. Por favor seleccione un número válido.")
                        continue

        except Exception as e:
            connection.rollback()
            return f"Error al interactuar con la base de datos: {e}"

# ----------------------------------------------------------------------------------------------------------------------
