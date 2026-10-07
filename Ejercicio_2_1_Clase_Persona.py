class Persona:
    """Representa los datos básicos de una persona."""
    def __init__(self, nombre, apellido, documento, nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.nacimiento = nacimiento
    def mostrar_datos(self):
        print(f"Nombre completo: {self.nombre} {self.apellido}")
        print(f"Documento: {self.documento}")
        print(f"Año de nacimiento: {self.nacimiento}")
        print("=" * 40)
def main():
    persona_a = Persona("Wolfgang", "Pineda", "1000000001", 2008)
    persona_b = Persona("Laura", "Martínez", "1000000002", 2007)
    print("PERSONA 1")
    persona_a.mostrar_datos()
    print("PERSONA 2")
    persona_b.mostrar_datos()
if __name__ == "__main__":
    main()
