class Alimentos:
    def __init__(self, nombre, calorias, proteinas, carbohidratos, grasas):
        self.nombre = nombre
        self.calorias = calorias
        self.proteinas = proteinas
        self.carbohidratos = carbohidratos
        self.grasas = grasas

    def imprimir_datos(self):
        print(
            f"Alimento: {self.nombre}, Calorías: {self.calorias} kcal, Proteínas: {self.proteinas} g, "
            f"Carbohidratos: {self.carbohidratos} g, Grasas: {self.grasas} g."
        )


alimento1 = Alimentos("Manzana", 52, 0.3, 14, 0.2)
alimento1.imprimir_datos()
