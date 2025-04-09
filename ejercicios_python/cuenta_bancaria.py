class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de {cantidad}. Nuevo saldo: {self.saldo}")
    
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente.")
    
    def mostrar_saldo(self):
        print(f"Saldo de la cuenta de {self.titular}: {self.saldo}")

class CuentaAhorros(Cuenta):
    def __init__(self, titular, saldo_inicial, tasa_interes):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes
    
    def aplicar_interes(self):
        interes = self.saldo * self.tasa_interes
        self.saldo += interes
        print(f"Interés aplicado: {interes}. Nuevo saldo: {self.saldo}")

class CuentaCorriente(Cuenta):
    def __init__(self, titular, saldo_inicial, limite_descuento):
        super().__init__(titular, saldo_inicial)
        self.limite_descuento = limite_descuento
    
    def retirar(self, cantidad):
        if cantidad <= self.saldo + self.limite_descuento:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente, incluyendo el límite de descuento.")

# Ejemplo de uso
cuenta_ahorros = CuentaAhorros("Juan", 1000, 0.05)
cuenta_corriente = CuentaCorriente("Sara", 500, 200)

cuenta_ahorros.mostrar_saldo()
cuenta_ahorros.aplicar_interes()

cuenta_corriente.mostrar_saldo()
cuenta_corriente.retirar(600)
