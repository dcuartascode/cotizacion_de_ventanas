class Naves:
    def __init__(self, ancho, largo):
        self.ancho = ancho
        self.largo = largo

    def perimetro(self):
        return 2 * (self.ancho + self.largo)

    def area_vidrio(self):
        # El vidrio es 1.5 cm más pequeño en cada lado
        return (self.ancho - 0.03) * (self.largo - 0.03)