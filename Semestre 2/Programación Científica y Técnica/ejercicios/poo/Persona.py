class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Mi Nombre es {self.nombre} y tengo {self.edad} años")


persona1 = Persona("Martin", 20)
persona2 = Persona("Martina", 25)
persona3 = Persona("Francisco", 30)
persona4 = Persona("Messi", 10)
persona1.presentarse()
persona2.presentarse()
persona3.presentarse()
persona4.presentarse()

