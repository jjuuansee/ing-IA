class Volador:
    def volar(self):
        print('Estoy volando')

class Nadador:
    def nadar(self):
        print('Estoy nadando')

class Pato(Volador, Nadador):
    def hacer_sonido(self):
        print('Cuac Cuac')

pato_amarillo = Pato()

pato_amarillo.hacer_sonido()
pato_amarillo.nadar()
pato_amarillo.volar()