class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Auto(Vehiculo):
    def atropellar_ciclista(self):
        print(f'Ciclista atropellado, {self.marca}, {self.modelo}')

class Moto(Vehiculo):
    def chocar_a_350(self):
        print(f'Aguante mirar las flores desde abajo {self.marca}, {self.modelo}')

class Avion(Vehiculo):
    def volar(self):
        print(f'Volar {self.marca}, {self.modelo}')


Auto1 = Auto('Mitsubishi', 'Lancer Evo X')
Moto1 = Moto('Kawaski', '!@(#!31')
Avion1 = Avion('Avioneta Crazy', 'Supercralifistilisticoespiralidozo')

Auto1.atropellar_ciclista()
Moto1.chocar_a_350()
Avion1.volar()