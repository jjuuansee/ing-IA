class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print('Guau')


class Gato(Animal):
    def hacer_sonido(self):
        print('Miau')

class Vaca(Animal):
    def hacer_sonido(self):
        print('Muuuuu!')

def hacer_sonidos(animales):
    for animal in animales:
        animal.hacer_sonido()


l = [Perro(), Gato(), Vaca()]
hacer_sonidos(l)
