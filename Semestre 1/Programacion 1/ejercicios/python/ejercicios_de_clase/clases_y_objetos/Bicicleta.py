class Bicicleta:
    def __init__(self, marca, color, tamano, tipo):
        self.marca = marca
        self.color = color
        self.tamano = tamano
        self.tipo = tipo

    # Métodos
    def get_marca(self):
        return self.marca

    def get_color(self):
        return self.color

    def get_tamano(self):
        return self.tamano

    def get_tipo(self):
        return self.tipo

    # Método para imprimir
    def __str__(self): # type: ignore
        print(f"Marca: {self.marca}\nColor: {self.color}\nTamaño: {self.tamano}\nTipo: {self.tipo}")


bicicleta1 = Bicicleta("GT", "Azul", "M", "MTB")
bicicleta1.__str__()
