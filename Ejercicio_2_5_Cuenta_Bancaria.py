from enum import Enum
class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"
class CuentaBancaria:
    def __init__(self, nombres, apellidos, numero, tipo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero = numero
        self.tipo = tipo
        self.saldo = 0.0
    def mostrar(self):
        print("INFORMACIÓN DE LA CUENTA")
        print(f"Titular: {self.nombres} {self.apellidos}")
        print(f"Número: {self.numero}")
        print(f"Tipo: {self.tipo.value}")
        print(f"Saldo: ${self.saldo:,.2f}")
        print("-" * 40)
    def consultar_saldo(self):
        print(f"Saldo disponible: ${self.saldo:,.2f}")
        return self.saldo
    def consignar(self, cantidad):
        if cantidad <= 0:
            print("La consignación debe ser mayor que cero.")
            return False
        self.saldo += cantidad
        print(f"Consignación realizada: ${cantidad:,.2f}")
        return True
    def retirar(self, cantidad):
        if cantidad <= 0:
            print("El retiro debe ser mayor que cero.")
            return False
        if cantidad > self.saldo:
            print("No hay saldo suficiente para realizar el retiro.")
            return False
        self.saldo -= cantidad
        print(f"Retiro realizado: ${cantidad:,.2f}")
        return True
def main():
    cuenta = CuentaBancaria(
        "Wolfgang",
        "Pineda",
        "010-458-729",
        TipoCuenta.AHORROS
    )
    cuenta.mostrar()
    print("Consignando $200.000...")
    cuenta.consignar(200000)
    cuenta.consultar_saldo()
    print("\nRetirando $70.000...")
    cuenta.retirar(70000)
    cuenta.consultar_saldo()
    print("\nIntentando retirar $200.000...")
    cuenta.retirar(200000)
    print("\nSaldo final:")
    cuenta.consultar_saldo()
if __name__ == "__main__":
    main()
