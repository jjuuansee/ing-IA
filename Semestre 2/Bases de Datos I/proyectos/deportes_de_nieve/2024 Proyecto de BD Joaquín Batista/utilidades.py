import re
from datetime import datetime, timedelta
import bcrypt

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- VALIDACIONES ---------------------------------------------------------

def validar_cedula(ci):
    """
    Valida que la cédula proporcionada cumpla con los criterios de formato y rango.

    Criterios de validación:
    - Debe ser un número de 7 u 8 dígitos.
    - Puede ser "0", lo que se considera como una entrada válida para cancelar.
    - Debe estar dentro del rango permitido de 3,000,000 a 70,000,000 (excluyendo "0").

    Parámetros:
    - ci (str): Cédula proporcionada como cadena de texto.

    Retorna:
    - bool: True si la cédula es válida según los criterios, False en caso contrario.
    """

    if ci == "0":
        return True

    # Verificar si es un número de 7 u 8 dígitos
    if not ci.isdigit() or not (7 <= len(ci) <= 8):
        return False

    # Convertir la cédula a un número entero y verificar si está dentro del rango permitido
    ci_num = int(ci)
    return 3000000 <= ci_num <= 70000000


def validar_nombre_apellido(cadena):
    """
    Valida que el nombre o apellido cumpla con los siguientes criterios:

    Criterios de validación:
    - Debe contener únicamente letras, espacios o guiones.
    - Puede incluir caracteres con acentos (á, é, í, ó, ú) y la letra ñ (mayúscula o minúscula).
    - La longitud total debe estar entre 2 y 50 caracteres.

    Parámetros:
    - cadena (str): El nombre o apellido que se desea validar.

    Retorna:
    - bool: True si la cadena cumple con todos los criterios de validación, False en caso contrario.
    """

    patron = r'^[A-Za-záéíóúÁÉÍÓÚñÑ]+([ -][A-Za-záéíóúÁÉÍÓÚñÑ]+)*$'
    return bool(re.match(patron, cadena)) and 2 <= len(cadena) <= 50


def validar_correo(correo):
    """
    Valida que el correo electrónico cumpla con los siguientes criterios:

    Criterios de validación:
    - Debe tener un formato válido (usuario@dominio.extensión).
    - Solo se permiten los dominios '@ucu.edu.uy' y '@correo.ucu.edu.uy'.

    Parámetros:
    - correo (str): El correo electrónico que se desea validar.

    Retorna:
    - bool: True si el correo cumple con el formato y pertenece a los dominios permitidos, False en caso contrario.
    """

    correo_patron = r'^[\w\.-]+@(ucu\.edu\.uy|correo\.ucu\.edu\.uy)$'
    return re.match(correo_patron, correo) is not None


def validar_contraseña(contraseña):
    """
    Valida que la contraseña cumpla con el requisito mínimo de longitud.

    Criterios de validación:
    - La contraseña debe tener al menos 6 caracteres.

    Parámetros:
    - contraseña (str): La contraseña que se desea validar.

    Retorna:
    - bool: True si la contraseña cumple con el criterio de longitud, False en caso contrario.
    """

    contraseña_patron = r'^.{6,}$'  # Contraseña: al menos 6 caracteres
    return re.match(contraseña_patron, contraseña) is not None


def validar_telefono(telefono):
    """
    Valida que el número de teléfono cumpla con el formato esperado.

    Criterios de validación:
    - El teléfono debe tener exactamente 9 dígitos.
    - Debe comenzar con '09'.

    Parámetros:
    - telefono (str): El número de teléfono que se desea validar.

    Retorna:
    - bool: True si el número de teléfono cumple con el formato especificado, False en caso contrario.
    """

    telefono_patron = r'^09\d{7}$'  # Formato: comienza con '09' y tiene exactamente 9 dígitos
    return re.match(telefono_patron, telefono) is not None


def validar_fecha_nacimiento(fecha_nac):
    """
    Valida que la fecha de nacimiento cumpla con los siguientes criterios:

    Criterios de validación:
    1. La fecha debe estar en el formato 'yyyy-mm-dd'.
    2. Debe ser una fecha válida en el calendario.
    3. El usuario debe tener al menos 18 años al momento de la validación.

    Parámetros:
    - fecha_nac (str): Fecha de nacimiento en formato 'yyyy-mm-dd'.

    Retorna:
    - bool: True si la fecha de nacimiento es válida y el usuario tiene al menos 18 años, False en caso contrario.
    """

    nac_patron = r'^(19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
    if re.match(nac_patron, fecha_nac):
        try:
            fecha_nacimiento = datetime.strptime(fecha_nac, '%Y-%m-%d')
            fecha_actual = datetime.now()
            edad = fecha_actual.year - fecha_nacimiento.year - (
                (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day)
            )
            return edad >= 18
        except ValueError:
            return False
    return False


def validar_hora(hora_str):
    """
    Valida que una hora proporcionada esté en el formato correcto (HH:MM)
    y dentro del rango permitido de 07:00 a 23:00.

    Parámetros:
    - hora_str (str): Hora en formato 'HH:MM'.

    Proceso de validación:
    1. Convierte la hora de entrada en un objeto datetime.
    2. Define los límites de validación: 07:00 (mínimo) y 23:00 (máximo).
    3. Verifica si la hora se encuentra dentro del rango definido.

    Retorna:
    - datetime: Objeto de hora válido si está dentro del rango.
    - None: Si la hora está fuera del rango o tiene un formato incorrecto.
    """

    try:
        hora = datetime.strptime(hora_str, '%H:%M')
        hora_min = datetime.strptime('07:00', '%H:%M')
        hora_max = datetime.strptime('23:00', '%H:%M')
        if hora_min <= hora <= hora_max:
            return hora
        else:
            return None
    except ValueError:
        return None


def validar_id(id_str):
    """
    Valida que una cadena de texto represente un ID válido.

    Parámetros:
    - id_str (str): La cadena de texto que representa el ID a validar.

    Proceso de validación:
    1. Comprueba si la cadena contiene solo dígitos.
    2. Convierte la cadena a un número entero y verifica que sea mayor a 0.

    Retorna:
    - True: Si el ID es un número entero positivo.
    - False: Si el ID no es válido (no numérico o menor o igual a 0).
    """

    return id_str.isdigit() and int(id_str) > 0


def hash_contraseñas(contraseña):
    """
    Hashea una contraseña utilizando bcrypt para garantizar la seguridad.

    Parámetros:
    - contraseña (str): La contraseña en texto plano que se desea hashear.

    Proceso:
    1. Se utiliza un patrón de encriptación fijo definido por `patron_de_encriptacion`.
    2. La contraseña es codificada y hasheada con el patrón mediante la biblioteca bcrypt.
    3. El resultado del hash se convierte a cadena de texto para facilitar su almacenamiento.

    Retorna:
    - contraseña_hash_str (str): La contraseña hasheada en formato de texto.

    Nota:
    Este método utiliza un patrón fijo para la sal de bcrypt, lo cual no es ideal en entornos de producción
    donde se debe usar una sal aleatoria generada automáticamente. Pero lo evitamos para evitar complejos
    """

    patron_de_encriptacion = b'$2b$12$1JP0hc5vdRYqK7gLQcX1y.'
    contraseña_hash = bcrypt.hashpw(contraseña.encode(), patron_de_encriptacion)
    contraseña_hash_str = contraseña_hash.decode('utf-8')
    return contraseña_hash_str

# ----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------- VALIDACIÓN DE INPUTS ------------------------------------------------

def solicitar_input_y_validarlo(mensaje, validacion, mensaje_error):
    """
    Solicita entrada al usuario y la valida utilizando una función de validación proporcionada.

    Parámetros:
    - mensaje (str): El mensaje que se muestra al usuario al solicitar la entrada.
    - validacion (funcion): Una función que toma un valor como argumento y retorna `True` si la entrada es válida, o `False` si no lo es.
    - mensaje_error (str): Mensaje que se muestra al usuario en caso de que la entrada no sea válida.

    Proceso:
    1. Solicita un valor al usuario mostrando el mensaje proporcionado.
    2. Valida la entrada utilizando la función `validacion`.
    3. Si la entrada no es válida, muestra el mensaje de error y solicita la entrada nuevamente.
    4. Repite este proceso hasta que se proporcione una entrada válida.

    Retorna:
    - valor (str): La entrada validada del usuario.
    """
    valor = input(mensaje)
    while not validacion(valor):
        print(mensaje_error)
        valor = input(mensaje)
    return valor