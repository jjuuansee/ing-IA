import os
import time
import questionary
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from conexion_bd import conectar_segun_rol, ejecutar_vista, ver_mis_clases
from utilidades import hash_contraseñas
from estructura.instructores import alta_instructor, baja_instructor, modificar_instructor
from estructura.alumnos import alta_alumno, baja_alumno, modificar_alumno
from estructura.turnos import alta_turnos, baja_turnos, modificar_turnos
from estructura.actividad_clase import modificar_actividad, modificar_clase
from estructura.alumno_clase import agregar_alumno_a_clase, eliminar_alumno_de_clase

# Crear una consola de Rich
console = Console()

def limpiar_consola():
    """Limpia la consola para mejorar la presentación."""
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception as e:
        console.print(f"[red]Error al limpiar la consola: {e}[/red]")


def iniciar_sesion():
    """
    Permite a los usuarios autenticarse en el sistema y determina su rol.
    Pasos:
        1. Solicita al usuario su correo y contraseña.
        2. Verifica que las credenciales sean válidas consultando la base de datos.
        3. Si el usuario tiene el rol de 'alumno', obtiene su cédula asociada.
        4. Retorna los datos relevantes para la sesión activa: rol, correo, ID de usuario y, en caso de ser 'alumno', su cédula.
    Retorno:
        - rol (str): Rol del usuario autenticado ('administrador', 'instructor' o 'alumno').
        - usuario (str): Correo electrónico del usuario autenticado.
        - id_usuario (int): ID del usuario en la tabla 'login'.
        - ci_usuario (int o None): Cédula asociada al usuario, solo si es 'alumno'.

    En caso de error o credenciales inválidas, retorna `None` en todos los campos.
    """

    try:
        connection = conectar_segun_rol('login')

        while True:
            limpiar_consola()
            console.print("[bold cyan]=== Bienvenido al sistema. Inicie sesión ===[/bold cyan]\n")
            modo = questionary.select(
                "Elija un modo:",
                choices=["Automatico", "Manual"]
            ).ask()

            if modo == "Automatico":
                opciones = [
                    "Administrador",
                    "Instructor",
                    "Alumno",
                ]

                rol = questionary.select(
                    "Elija un rol:",
                    choices=opciones
                ).ask()

                if rol == "Administrador":
                    usuario = "cristian.dinardi@ucu.edu.uy"
                    contraseña_hasheada = hash_contraseñas("passcristian95")

                elif rol == "Instructor":
                    usuario = "maria.lopez@ucu.edu.uy"
                    contraseña_hasheada = hash_contraseñas("passmaria456")

                elif rol == "Alumno":
                    usuario = "juan.perez@ucu.edu.uy"
                    contraseña_hasheada = hash_contraseñas("passjuan123")

            elif modo == "Manual":
                usuario = Prompt.ask("Ingrese su correo")
                contraseña = Prompt.ask("Ingrese su contraseña", password=True)
                contraseña_hasheada = hash_contraseñas(contraseña)

            with connection.cursor() as cursor:
                # Verificar login y obtener rol
                query = "SELECT id, contraseña, rol FROM login WHERE correo = %s AND fecha_de_baja IS NULL"
                cursor.execute(query, (usuario,))
                resultado = cursor.fetchone()

                if resultado:
                    id_usuario, contraseña_db, rol = resultado
                    if contraseña_hasheada == contraseña_db:
                        # Consultar la cédula según el rol
                        ci_usuario = None
                        if rol == 'alumno':
                            query_ci = "SELECT ci FROM alumnos WHERE id_login = %s AND fecha_de_baja IS NULL"
                        elif rol == 'instructor':
                            query_ci = "SELECT ci FROM instructores WHERE id_login = %s AND fecha_de_baja IS NULL"
                        else:
                            query_ci = None

                        if query_ci:
                            cursor.execute(query_ci, (id_usuario,))
                            resultado_ci = cursor.fetchone()
                            if resultado_ci:
                                ci_usuario = resultado_ci[0]

                        console.print(f"[bold green]\nInicio de sesión exitoso[/bold green]. Bienvenido/a, "
                                      f"[yellow]{usuario}[/yellow]. Rol: [cyan]{rol.capitalize()}[/cyan]")
                        Prompt.ask("Presione Enter para continuar...")
                        return rol, usuario, id_usuario, ci_usuario
                    else:
                        console.print("[bold red]\nContraseña incorrecta. Inténtelo nuevamente.[/bold red]")
                else:
                    console.print(
                        "[bold red]\nCorreo no registrado o cuenta inactiva. Inténtelo nuevamente.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]\nError durante el inicio de sesión: {e}[/bold red]")
        return None, None, None, None


def menu_principal(connection, rol, ci_usuario=None):
    """
    Presenta el menú principal al usuario según su rol y redirige a las operaciones correspondientes.

    Parámetros:
        - connection: Conexión activa a la base de datos.
        - rol: Rol del usuario autenticado ('administrador', 'instructor' o 'alumno').
        - ci_usuario: (Opcional) Cédula del usuario, solo necesaria si el rol es 'alumno'.

    Descripción:
        - Muestra una tabla de opciones personalizada basada en el rol del usuario.
        - Permite seleccionar y ejecutar operaciones específicas, como alta, baja, modificación de datos o generación de reportes.
        - Ofrece una opción para cerrar el programa.
        - Realiza validaciones para manejar opciones inválidas.
    """

    while True:
        limpiar_consola()
        console.print(f"[bold magenta]=== Menú Principal - Rol: {rol.capitalize()} ===[/bold magenta]\n")

        # Crear tabla para mostrar las opciones
        table = Table(title="Opciones del Menú", show_header=True, header_style="bold blue")
        table.add_column("Opción", justify="center")
        table.add_column("Descripción", justify="left")

        # Opciones según el rol
        opciones = {
            "administrador": [
                ("1", "Alta de Instructor"),
                ("2", "Baja de Instructor"),
                ("3", "Modificar Instructor"),
                ("4", "Alta de Alumno"),
                ("5", "Baja de Alumno"),
                ("6", "Modificar Alumno"),
                ("7", "Alta de Turno"),
                ("8", "Baja de Turno"),
                ("9", "Modificar Turno"),
                ("10", "Modificar Actividad"),
                ("11", "Modificar Clase"),
                ("12", "Agregar Alumno a Clase"),
                ("13", "Eliminar Alumno de Clase"),
                ("14", "Sistema de Reportes"),
                ("0", "Salir"),
            ],
            "instructor": [
                ("1", "Agregar Alumno a Clase"),
                ("2", "Eliminar Alumno de Clase"),
                ("3", "Ver Mis Clases"),
                ("0", "Salir"),
            ],
            "alumno": [
                ("1", "Agregarme a una Clase"),
                ("2", "Eliminarme de una Clase"),
                ("3", "Ver Mis Clases"),
                ("0", "Salir"),
            ],
        }

        # Agregar las opciones a la tabla
        for opcion, descripcion in opciones[rol]:
            table.add_row(opcion, descripcion)

        # Mostrar tabla
        console.print(table)

        # Pedir al usuario una opción
        opcion = Prompt.ask("\nSeleccione una opción")

        if rol == "administrador":
            if opcion == "1":
                ejecutar_funcion(alta_instructor, connection)
            elif opcion == "2":
                ejecutar_funcion(baja_instructor, connection)
            elif opcion == "3":
                ejecutar_funcion(modificar_instructor, connection)
            elif opcion == "4":
                ejecutar_funcion(alta_alumno, connection)
            elif opcion == "5":
                ejecutar_funcion(baja_alumno, connection)
            elif opcion == "6":
                ejecutar_funcion(modificar_alumno, connection)
            elif opcion == "7":
                ejecutar_funcion(alta_turnos, connection)
            elif opcion == "8":
                ejecutar_funcion(baja_turnos, connection)
            elif opcion == "9":
                ejecutar_funcion(modificar_turnos, connection)
            elif opcion == "10":
                ejecutar_funcion(modificar_actividad, connection)
            elif opcion == "11":
                ejecutar_funcion(modificar_clase, connection)
            elif opcion == "12":
                ejecutar_funcion(agregar_alumno_a_clase, connection, ci_usuario, rol)
            elif opcion == "13":
                ejecutar_funcion(eliminar_alumno_de_clase, connection, ci_usuario, rol)
            elif opcion == "14":
                menu_vistas(connection)
            elif opcion == "0":
                console.print("\n[bold yellow]Cerrando el programa...[/bold yellow]")
                time.sleep(2)
                break
            else:
                console.print("[bold red]\nOpción inválida. Inténtelo de nuevo.[/bold red]")

        elif rol == "instructor":
            if opcion == "1":
                ejecutar_funcion(agregar_alumno_a_clase, connection, ci_usuario, rol)
            elif opcion == "2":
                ejecutar_funcion(eliminar_alumno_de_clase, connection, ci_usuario, rol)
            elif opcion == "3":
                ejecutar_funcion(ver_mis_clases, connection, rol, ci_usuario)
            elif opcion == "0":
                console.print("\n[bold yellow]Cerrando el programa...[/bold yellow]")
                break
            else:
                console.print("[bold red]\nOpción inválida. Inténtelo de nuevo.[/bold red]")

        elif rol == "alumno":
            if opcion == "1":
                ejecutar_funcion(agregar_alumno_a_clase, connection, ci_usuario, rol)
            elif opcion == "2":
                ejecutar_funcion(eliminar_alumno_de_clase, connection, ci_usuario, rol)
            elif opcion == "3":
                ejecutar_funcion(ver_mis_clases, connection, rol, ci_usuario)
            elif opcion == "0":
                console.print("\n[bold yellow]Cerrando el programa...[/bold yellow]")
                break
            else:
                console.print("[bold red]\nOpción inválida. Inténtelo de nuevo.[/bold red]")


def menu_vistas(connection):
    """
    Muestra un menú para que el administrador consulte los reportes generados a partir de las vistas.

    Parámetros:
        - connection: Conexión activa a la base de datos.

    Descripción:
        - Ofrece opciones para consultar diferentes vistas predefinidas:
            1. Actividades con más alumnos.
            2. Turnos con más clases dictadas.
            3. Actividades que más ingresos generan.
        - Permite visualizar los resultados de cada vista en formato legible utilizando Rich.
        - Brinda la opción de regresar al menú principal.
        - Valida las entradas del usuario para manejar opciones inválidas.
    """

    while True:
        limpiar_consola()
        console.print("[bold magenta]=== Sistema de Reportes ===[/bold magenta]\n")

        table = Table(title="Opciones de Reportes", show_header=True, header_style="bold blue")
        table.add_column("Opción", justify="center")
        table.add_column("Descripción", justify="left")
        opciones = [
            ("1", "Actividades con más alumnos"),
            ("2", "Turnos con más clases dictadas"),
            ("3", "Actividades que más ingresos generan"),
            ("0", "Volver al menú principal")
        ]
        for opcion, descripcion in opciones:
            table.add_row(opcion, descripcion)

        console.print(table)
        opcion = Prompt.ask("Seleccione una opción")

        if opcion == '1':
            resultado = ejecutar_vista(connection, "actividades_con_mas_alumnos")
            console.print(resultado)
            Prompt.ask("\nPresione Enter para volver al menú de reportes...")
        elif opcion == '2':
            resultado = ejecutar_vista(connection, "turnos_con_mas_clases_dictadas")
            console.print(resultado)
            Prompt.ask("\nPresione Enter para volver al menú de reportes...")
        elif opcion == '3':
            resultado = ejecutar_vista(connection, "actividades_que_mas_ingresos_generan")
            console.print(resultado)
            Prompt.ask("\nPresione Enter para volver al menú de reportes...")
        elif opcion == '0':
            break
        else:
            console.print("[bold red]Opción inválida. Inténtalo de nuevo.[/bold red]")


def ejecutar_funcion(funcion, *args):
    """
    Ejecuta una función proporcionada y muestra el resultado al usuario.

    Parámetros:
        - funcion: Función que se desea ejecutar.
        - *args: Todos los argumentos necesarios para la ejecución de la función.

    Descripción:
        - Limpia la consola antes de ejecutar la función para mejorar la presentación.
        - Muestra un encabezado indicando que se está ejecutando una operación.
        - Captura y muestra el resultado de la función en formato legible.
        - Pausa la ejecución hasta que el usuario presione Enter, para permitir la lectura del resultado.
    """

    limpiar_consola()
    console.print("[bold cyan]=== Ejecutando operación ===[/bold cyan]\n")
    resultado = funcion(*args)
    console.print(f"[bold green]{resultado}[/bold green]")
    Prompt.ask("\nPresione Enter para continuar...")

# Inicio de sesión y ejecución del menú principal
rol, usuario, id_usuario, ci_usuario = iniciar_sesion()
if rol:
    connection = conectar_segun_rol(rol)
    try:
        menu_principal(connection, rol, ci_usuario)
    finally:
        connection.close()
        console.print("\n[bold green]Conexión cerrada correctamente.[/bold green]")
