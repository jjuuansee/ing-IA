# Schema Biblioteca:
# ------------------------------------------------------------------------------------------------
class Libro:
    def __init__(self, Titulo, ISBN):
        self.Titulo = Titulo
        self.ISBN = ISBN
        self.Disponible = True

    def __str__(self):
        return f"Titulo: {self.Titulo}, ISBN: {self.ISBN}, Disponible: {self.Disponible}"

    def cambiar_estado(self):
        if self.Disponible:
            self.Disponible = False
        else:
            self.Disponible = True
# ------------------------------------------------------------------------------------------------


class Autor:
    def __init__(self, Nombre, Nacionalidad):
        self.Nombre = Nombre
        self.Nacionalidad = Nacionalidad

    def __str__(self):
        return f"Nombre autor: {self.Nombre}, Nacionalidad: {self.Nacionalidad}"
# ------------------------------------------------------------------------------------------------


class Cliente:
    def __init__(self, Nombre, Email, Numero_cliente):
        self.Nombre = Nombre
        self.Email = Email
        self.Numero_cliente = Numero_cliente
        self.prestamos_disponibles = []

    def __str__(self):
        return f"Nombre: {self.Nombre}, Email: {self.Email}, Numero_cliente: {self.Numero_cliente}"

    def agregar_prestamo(self):
        if len(self.prestamos_disponibles) <= 3:
            self.prestamos_disponibles.append(Prestamo())
# ------------------------------------------------------------------------------------------------


class Prestamo:
    def __init__(self, Cliente, Libro, Fecha_prestamo, Fecha_devolucion):
        self.Cliente = Cliente
        self.Libro = Libro
        self.Fecha_prestamo = Fecha_prestamo
        self.Fecha_devolucion = Fecha_devolucion

    def __str__(self):
        return f"Fecha_prestamo: {self.Fecha_prestamo}, Fecha_devolucion: {self.Fecha_devolucion}"

 #   def realizar_prestamo(self):
# ------------------------------------------------------------------------------------------------
