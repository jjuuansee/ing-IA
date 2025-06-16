class Empleado:
    def __init__(self, nombre, salario, dias_vacaiones):
        self.dias_vacaciones = 0
        self.nombre = nombre
        self.salario = salario
        self.dias_vacaiones = dias_vacaiones

    def trabajar(self):
        return f'{self.nombre} está trabajando'

    def tomar_vacaciones(self,dias):
        if dias > 0:
            self.dias_vacaciones = dias
            return f'Tus vacaciones seran de {self.dias_vacaciones} dias!'
        else:
            return 'Los dias no pueden ser negativos'

    def __str__(self):
        return f'Empleado: {self.nombre}, Salario: {self.salario}, Dias vacaciones: {self.dias_vacaciones}'


empleado1 = Empleado('Juan',  2000, 5)
print(empleado1.tomar_vacaciones(50))
print(empleado1.trabajar())
print(empleado1.__str__())