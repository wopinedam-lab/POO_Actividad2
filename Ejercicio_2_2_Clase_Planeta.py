from enum import Enum
class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"
class Planeta:
    """Almacena las características principales de un planeta."""
    UA_EN_KM = 149_597_870
    def __init__(
        self,
        nombre,
        satelites,
        masa,
        volumen,
        diametro,
        distancia_sol,
        tipo,
        observable
    ):
        self.nombre = nombre
        self.satelites = satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.observable = observable
    def densidad(self):
        if self.volumen == 0:
            return 0
        return self.masa / self.volumen
    def es_exterior(self):
        distancia_km = self.distancia_sol * 1_000_000
        distancia_ua = distancia_km / self.UA_EN_KM
        return distancia_ua > 3.4
    def mostrar(self):
        print(f"Planeta: {self.nombre}")
        print(f"Satélites: {self.satelites}")
        print(f"Masa: {self.masa:.4e} kg")
        print(f"Volumen: {self.volumen:.4e} km³")
        print(f"Diámetro: {self.diametro} km")
        print(f"Distancia al Sol: {self.distancia_sol} millones de km")
        print(f"Tipo: {self.tipo.value}")
        print(f"Observable: {'Sí' if self.observable else 'No'}")
        print(f"Densidad: {self.densidad():.4e} kg/km³")
        print(f"¿Es exterior?: {'Sí' if self.es_exterior() else 'No'}")
        print("-" * 40)
def main():
    tierra = Planeta(
        "Tierra", 1, 5.9736e24, 1.08321e12, 12742,
        150, TipoPlaneta.TERRESTRE, True
        )
    saturno = Planeta(
        "Saturno", 146, 5.6834e26, 8.2713e14, 116460,
        1433, TipoPlaneta.GASEOSO, True
    )
    tierra.mostrar()
    saturno.mostrar()
if __name__ == "__main__":
    main()
