import pymysql

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------- CONEXIÓN A LA BD ---------------------------------------------------
def conectar_segun_rol(rol):
    """
    Crea una conexión a la base de datos utilizando las credenciales específicas de cada rol.

    Parámetros:
        - rol (str): El rol del usuario que intenta conectarse a la base de datos. Puede ser:
            - 'administrador'
            - 'instructor'
            - 'alumno'
            - 'login'.

    Comportamiento:
        - Valida que el rol proporcionado exista en el diccionario `credenciales`.
        - Establece una conexión a la base de datos utilizando las credenciales asociadas al rol.
        - Si el rol no es válido, lanza un ValueError.
        - Si ocurre un error de conexión con la base de datos, captura y vuelve a lanzar el error.

    Retorno:
        - Una conexión activa a la base de datos para el rol especificado.

    Excepciones:
        - ValueError: Si el rol no es reconocido.
        - pymysql.MySQLError: Sí ocurre un error durante la conexión a la base de datos.
    """

    credenciales = {
        'administrador': {'user': 'administrador', 'password': 'AAJ-394monoia'},
        'instructor': {'user': 'instructor', 'password': 'Instruc_najuale'},
        'alumno': {'user': 'alumno', 'password': 'Estudio231564'},
        'login': {'user': 'login', 'password': 'LogDepNev2024JAI'},
    }

    if rol not in credenciales:
        raise ValueError("Rol desconocido.")

    try:
        return pymysql.connect(
            host='localhost',
            user=credenciales[rol]['user'],
            password=credenciales[rol]['password'],
            db='deportes_de_nieve',
            cursorclass = pymysql.cursors.DictCursor
                                )
    except pymysql.MySQLError as e:
        print(f"Error al conectar con la base de datos: {e}")
        raise

def cerrar_conexion(connection):
    """
    Cierra una conexión a la base de datos si está abierta.
    """
    if connection:
        try:
            connection.close()
            print("Conexión cerrada correctamente.")
        except Exception as e:
            print(f"Error al cerrar la conexión: {e}")


# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------- EXISTENCIA DE PARÁMETROS EN LA BASE DE DATOS --------------------------------------

def verificar_existencia_en_tabla(connection, valor, tabla, columna="id"):
    """
    Verifica si un valor específico existe en una columna de una tabla y que no esté dado de baja.

    Parámetros:
        - connection: Objeto de conexión a la base de datos.
        - valor: El valor a buscar en la columna especificada.
        - tabla (str): Nombre de la tabla donde se realizará la búsqueda.
        - columna (str, opcional): Nombre de la columna donde se verificará el valor.
                                    Por defecto es 'id'.

    Comportamiento:
        - Construye y ejecuta una consulta SQL para verificar si el valor especificado
          existe en la columna y si no tiene una fecha de baja (`fecha_de_baja IS NULL`).
        - Retorna `True` si el valor existe y no está dado de baja.
        - Retorna `False` si el valor no existe, está dado de baja o si ocurre un error durante la consulta.

    Retorno:
        - bool: `True` si el valor existe y está activo, `False` en caso contrario.

    Excepciones manejadas:
        - pymysql.MySQLError: Si ocurre un error durante la ejecución de la consulta,
          se imprime el error y se retorna `False`.
    """

    try:
        with connection.cursor() as cursor:
            query = f"SELECT 1 FROM {tabla} WHERE {columna} = %s AND fecha_de_baja IS NULL"
            cursor.execute(query, (valor,))
            return cursor.fetchone() is not None
    except pymysql.MySQLError as e:
        print(f"Error al verificar la existencia en la tabla: {e}")
        return False

def validar_clase_no_solapada(cursor, clase_id, ci_alumno):
    """
    Valida que un alumno no tenga conflictos de horarios al inscribirse en una nueva clase.

    Parámetros:
        - cursor: Objeto cursor de la conexión a la base de datos para ejecutar las consultas SQL.
        - clase_id (int): ID de la clase que se desea verificar.
        - ci_alumno (int): Cédula del alumno que se está intentando inscribir.

    Comportamiento:
        1. Consulta el horario (hora_inicio y hora_fin) de la clase especificada por `clase_id`.
        2. Recupera los horarios de todas las clases activas en las que el alumno (`ci_alumno`) ya está inscrito.
        3. Compara el horario de la nueva clase con los horarios existentes para identificar posibles solapamientos:
           - Si las horas de inicio y fin de la nueva clase no se cruzan con ninguna otra clase del alumno, no hay conflicto.
           - Si hay solapamiento, retorna `False`.

    Retorno:
        - bool: `True` si no hay conflictos de horarios; `False` si hay un solapamiento o si ocurre un error.

    Excepciones manejadas:
        - Se captura cualquier excepción que ocurra durante la ejecución de las consultas SQL.
          En caso de error, se imprime el mensaje y se retorna `False`.
    """

    try:
        # Obtener el turno de la nueva clase
        query_turno_clase = """
            SELECT t.hora_inicio, t.hora_fin
            FROM clase c
            JOIN turnos t ON c.id_turno = t.id
            WHERE c.id = %s AND c.fecha_de_baja IS NULL
        """
        cursor.execute(query_turno_clase, (clase_id,))
        turno_clase = cursor.fetchone()

        if not turno_clase:
            return False  # No se pudo obtener el turno de la clase

        hora_inicio_clase, hora_fin_clase = turno_clase

        # Verificar solapamientos con otras clases del alumno
        query_turnos_alumno = """
            SELECT t.hora_inicio, t.hora_fin
            FROM alumno_clase ac
            JOIN clase c ON ac.id_clase = c.id
            JOIN turnos t ON c.id_turno = t.id
            WHERE ac.ci_alumno = %s AND c.fecha_de_baja IS NULL
        """
        cursor.execute(query_turnos_alumno, (ci_alumno,))
        turnos_alumno = cursor.fetchall()

        # Validar solapamientos
        for turno in turnos_alumno:
            hora_inicio, hora_fin = turno
            if not (hora_fin_clase <= hora_inicio or hora_inicio_clase >= hora_fin):
                return False  # Hay un solapamiento de horarios

        return True  # No hay solapamientos
    except Exception as e:
        print(f"Error al validar solapamientos: {e}")
        return False

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------- INTERACCIONES CON LAS VISTAS -----------------------------------------------

def ejecutar_vista(connection, vista):
    """
    Ejecuta una vista SQL y devuelve sus resultados en formato legible.

    Parámetros:
        - connection: Objeto de conexión a la base de datos que permite ejecutar las consultas SQL.
        - vista (str): Nombre de la vista SQL que se desea consultar.

    Comportamiento:
        1. Construye una consulta SQL para seleccionar todos los datos de la vista especificada.
        2. Ejecuta la consulta utilizando el cursor de la conexión a la base de datos.
        3. Si la vista no contiene resultados, retorna un mensaje indicando que no se encontraron datos.
        4. Si la vista devuelve resultados:
           - Obtiene los nombres de las columnas desde la descripción del cursor.
           - Formatea los resultados en una tabla de texto con encabezados y filas separadas por delimitadores.
        5. Retorna el contenido formateado como una cadena legible.

    Retorno:
        - str: Contenido de la vista en formato de texto legible o un mensaje indicando que no se encontraron resultados.

    Excepciones manejadas:
        - Si ocurre un error durante la ejecución de la consulta, captura la excepción y retorna un mensaje de error con detalles.
    """

    try:
        with connection.cursor() as cursor:
            query = f"SELECT * FROM {vista};"
            cursor.execute(query)
            resultados = cursor.fetchall()

            if not resultados:
                return f"No se encontraron resultados para la vista '{vista}'."

            columnas = [desc[0] for desc in cursor.description]  # Nombres de columnas
            reporte = "\n".join(
                " | ".join(map(str, fila)) for fila in resultados
            )
            return f"Resultados de '{vista}':\n" + " | ".join(columnas) + "\n" + reporte

    except Exception as e:
        return f"Error al ejecutar la vista '{vista}': {e}"

# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------- VER MIS CLASES ---------------------------------------------------

def ver_mis_clases(connection, rol, ci_usuario=None):
    """
    Muestra las clases a las que está inscrito un alumno o las que dictará un instructor.
    Parámetros:
        - connection: conexión activa a la base de datos.
        - rol: rol del usuario ('alumno' o 'instructor').
        - ci_usuario: cédula del usuario (requerida si el rol es 'alumno' o 'instructor').
    """
    try:
        with connection.cursor() as cursor:
            if rol == 'alumno':
                if not ci_usuario:
                    return "Error: No se obtuvo la cédula para el alumno."

                query = """
                    SELECT c.id AS clase_id, a.descripcion AS actividad, t.hora_inicio, t.hora_fin
                    FROM alumno_clase ac
                    JOIN clase c ON ac.id_clase = c.id
                    JOIN actividades a ON c.id_actividad = a.id
                    JOIN turnos t ON c.id_turno = t.id
                    WHERE ac.ci_alumno = %s AND c.fecha_de_baja IS NULL AND t.fecha_de_baja IS NULL
                """
                cursor.execute(query, (ci_usuario,))
                clases = cursor.fetchall()

                if not clases:
                    return "No estás inscrito/a en ninguna clase activa."

                # Mostrar las clases inscritas
                mensaje = "[bold cyan]Clases en las que estás inscrito/a:[/bold cyan]\n"
                for clase in clases:
                    mensaje += (
                        f"- Clase ID: {clase['clase_id']}\n"
                        f"  Actividad: {clase['actividad']}\n"
                        f"  Horario: {clase['hora_inicio']} - {clase['hora_fin']}\n"
                    )
                return mensaje

            elif rol == 'instructor':
                if not ci_usuario:
                    return "Error: No se proporcionó la cédula para el instructor."

                query = """
                    SELECT c.id AS clase_id, a.descripcion AS actividad, t.hora_inicio, t.hora_fin
                    FROM clase c
                    JOIN actividades a ON c.id_actividad = a.id
                    JOIN turnos t ON c.id_turno = t.id
                    WHERE c.ci_instructor = %s AND c.fecha_de_baja IS NULL AND t.fecha_de_baja IS NULL
                """
                cursor.execute(query, (ci_usuario,))
                clases = cursor.fetchall()

                if not clases:
                    return "No tienes ninguna clase asignada para dictar."

                # Mostrar las clases que va a dictar
                mensaje = "[bold cyan]Clases asignadas para dictar:[/bold cyan]\n"
                for clase in clases:
                    mensaje += (
                        f"- Clase ID: {clase['clase_id']}\n"
                        f"  Actividad: {clase['actividad']}\n"
                        f"  Horario: {clase['hora_inicio']} - {clase['hora_fin']}\n"
                    )
                return mensaje

            else:
                return "Rol no válido. Solo 'alumno' o 'instructor' pueden ver sus clases."

    except Exception as e:
        return f"Error al consultar las clases: {e}"
