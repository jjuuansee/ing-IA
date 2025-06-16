class Proyecto:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion
        self.equipo = []

    def agregar_miembro(self):
        seguir = True
        while seguir:
            print('Para dejar de ingresar miembros ingrese (Salir)')
            miembro = input('Ingrese los nombres del equipo: ').title()
            if miembro == 'Salir':
                seguir = False
            else:
                self.equipo.append(miembro)
        print(f'El equipo esta conformado por: {self.equipo}')

    def extender_duracion(self, dias):
        self.duracion += dias
        print(f'La duracion es de: {self.duracion}')

    def __str__(self):
        return f'Nombre: {self.nombre}, Duracion: {self.duracion}, Equipo: {self.equipo}'


proyecto = Proyecto('Lights Out!', 30)
proyecto.agregar_miembro()
proyecto.extender_duracion(5)
print(proyecto.__str__())