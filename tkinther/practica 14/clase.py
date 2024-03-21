class Cuenta:
    def __init__(self, numero_cuenta, titular, edad, saldo=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.edad = edad
        self.saldo = saldo

    def consultar_saldo(self):
        return self.saldo

    def ingresar_efectivo(self, cantidad):
        self.saldo += cantidad

    def retirar_efectivo(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            raise ValueError("Fondos insuficientes.")

    def depositar_en_otra_cuenta(self, cuenta_destino, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            cuenta_destino.ingresar_efectivo(cantidad)
        else:
            raise ValueError("Fondos insuficientes.")
        
   