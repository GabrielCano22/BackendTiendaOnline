class Alimentos:
    def __init__(self, nombre, calorias, proteinas, carbohidratos, grasas):
        self.nombre = nombre
        self.calorias = calorias
        self.proteinas = proteinas
        self.carbohidratos = carbohidratos
        self.grasas = grasas

    def imprimir_datos(self):
        print(
            f"{self.nombre}: {self.calorias} kcal, {self.proteinas} g proteínas, "
            f"{self.carbohidratos} g carbohidratos, {self.grasas} g grasas"
        )


alimento1 = Alimentos("Manzana", 52, 0.3, 14, 0.2)
alimento1.imprimir_datos()
