class CuentaBancaria:
    def __init__(self, num_cuenta, saldo):
        self.num_cuenta = num_cuenta
        self.__saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f'El saldo de la cuenta {self.num_cuenta} ahora es: {self.__saldo}')
        else:
            print('El monto no es valido')

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f'La transaccion fue realizada con exito. El saldo de la cuenta {self.num_cuenta} es de: {self.__saldo}')
        elif monto > self.__saldo:
            print('Saldo insuficiente para realizar la transaccion')
        elif monto <= 0:
            print('Monto invalido')

    def get_saldo(self):
        print(self.__saldo)

    def set_saldo(self, monto):
        if monto > 0:
            self.__saldo = monto
            print(f'El saldo ha sido modificado! Tu saldo ahora es {self.__saldo}')
        else:
            print('El saldo es invalido')


Cuenta1 = CuentaBancaria(1, 100)
Cuenta2 = (CuentaBancaria(2, 300))
#Cuenta1.depositar(100)
#Cuenta2.retirar(300)
Cuenta1.get_saldo()
Cuenta2.set_saldo(400)
