class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def __str__(self):
        return f'Soy {self.nombre} y mi sueldo es de {self.salario}'

class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, salario, duracion_contrato):
        super().__init__(nombre, salario)
        self.duracion = duracion_contrato

    def __str__(self):
        return super().__str__() + f', Contrato hasta: {self.duracion}'

class EmpleadoPermanente(Empleado):
    def __init__(self, nombre, salario, beneficios):
        super().__init__(nombre, salario)
        self.beneficios = beneficios

    def __str__(self):
        return super().__str__() + f', Beneficios: {self.beneficios}'

empleado_temp = EmpleadoTemporal('Juan', '1500', '1 año')
empleado_perm = EmpleadoPermanente('Diego', '3000', 'Seguro medico')
print(empleado_perm)
print(empleado_temp)