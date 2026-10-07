from enum import Enum
class Combustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas natural"
class CategoriaAuto(Enum):
    CIUDAD = "Carro de ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"
class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"
class Automovil:
    """Modelo sencillo de un automóvil y su velocidad."""
    def __init__(
        self, marca, modelo, motor, combustible, categoria,
        puertas, asientos, velocidad_maxima, color
    ):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.combustible = combustible
        self.categoria = categoria
        self.puertas = puertas
        self.asientos = asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad = 0.0
    def establecer_velocidad(self, nueva_velocidad):
        if nueva_velocidad < 0:
            self.velocidad = 0.0
        elif nueva_velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
        else:
            self.velocidad = nueva_velocidad
    def acelerar(self, aumento):
        self.establecer_velocidad(self.velocidad + aumento)
    def desacelerar(self, disminucion):
        self.establecer_velocidad(self.velocidad - disminucion)
    def frenar(self):
        self.velocidad = 0.0
    def tiempo_recorrido(self, distancia):
        if self.velocidad <= 0:
            return 0.0
        return distancia / self.velocidad
    def mostrar(self):
        print("DATOS DEL AUTOMÓVIL")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor} L")
        print(f"Combustible: {self.combustible.value}")
        print(f"Categoría: {self.categoria.value}")
        print(f"Puertas: {self.puertas}")
        print(f"Asientos: {self.asientos}")
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")
        print(f"Color: {self.color.value}")
        print(f"Velocidad actual: {self.velocidad} km/h")
        print("-" * 40)
def main():
    auto = Automovil(
        "Mazda", 2022, 2.0, Combustible.GASOLINA,
        CategoriaAuto.SUV, 5, 5, 190.0, Color.AZUL
    )
    auto.mostrar()
    auto.establecer_velocidad(90)
    print(f"Velocidad inicial: {auto.velocidad} km/h")
    auto.acelerar(30)
    print(f"Después de acelerar: {auto.velocidad} km/h")
    auto.desacelerar(40)
    print(f"Después de desacelerar: {auto.velocidad} km/h")
    distancia = 100
    print(f"Tiempo para recorrer {distancia} km: "
          f"{auto.tiempo_recorrido(distancia):.2f} horas")
    auto.frenar()
    print(f"Después de frenar: {auto.velocidad} km/h")
if __name__ == "__main__":
    main()
