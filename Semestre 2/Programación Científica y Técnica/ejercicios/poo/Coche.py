class Coche:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    def getMarca(self):
        print(self.__marca)

    def getModelo(self):
        print(self.__modelo)

    def getAño(self):
        print(self.__año)

    def setMarca(self, marca):
        self.__marca = marca

    def setModelo(self, modelo):
        self.__modelo = modelo

    def setAño(self, año):
        self.__año = año

    def descripcion(self):
        print(f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__año}")


coche1 = Coche('Mitsubishi', 'Lancer Evo X', 2010)
coche1.getAño()
coche1.getMarca()
coche1.getModelo()
coche1.descripcion()
3