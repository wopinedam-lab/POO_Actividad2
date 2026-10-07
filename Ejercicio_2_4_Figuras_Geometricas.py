import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * self.radio ** 2
    def perimetro(self):
        return 2 * math.pi * self.radio
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * (self.base + self.altura)
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2
    def perimetro(self):
        return 4 * self.lado
class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2
    def hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)
    def perimetro(self):
        return self.base + self.altura + self.hipotenusa()
    def tipo(self):
        lados = [self.base, self.altura, self.hipotenusa()]
        if math.isclose(lados[0], lados[1]) and math.isclose(lados[1], lados[2]):
            return "Equilátero"
        if (
            math.isclose(lados[0], lados[1])
            or math.isclose(lados[0], lados[2])
            or math.isclose(lados[1], lados[2])
        ):
            return "Isósceles"
        return "Escaleno"
def main():
    figuras = [
        Circulo(4),
        Rectangulo(7, 3),
        Cuadrado(5),
        TrianguloRectangulo(3, 4)
    ]
    circulo = figuras[0]
    print("CÍRCULO")
    print(f"Área: {circulo.area():.2f} cm²")
    print(f"Perímetro: {circulo.perimetro():.2f} cm")
    print()
    rectangulo = figuras[1]
    print("RECTÁNGULO")
    print(f"Área: {rectangulo.area():.2f} cm²")
    print(f"Perímetro: {rectangulo.perimetro():.2f} cm")
    print()
    cuadrado = figuras[2]
    print("CUADRADO")
    print(f"Área: {cuadrado.area():.2f} cm²")
    print(f"Perímetro: {cuadrado.perimetro():.2f} cm")
    print()
    triangulo = figuras[3]
    print("TRIÁNGULO RECTÁNGULO")
    print(f"Área: {triangulo.area():.2f} cm²")
    print(f"Hipotenusa: {triangulo.hipotenusa():.2f} cm")
    print(f"Perímetro: {triangulo.perimetro():.2f} cm")
    print(f"Tipo: {triangulo.tipo()}")
if __name__ == "__main__":
    main()
