class Ventana:
    ESTILOS_VALIDOS = ["O", "XO", "OXXO", "OXO"]
    ACABADOS_ALUMINIO = ["Pulido", "Lacado Brillante", "Lacado Mate", "Anodizado"]
    TIPOS_VIDRIO = ["Transparente", "Bronce", "Azul"]

    def __init__(self, ancho, largo, estilo, cantidad, estado_ventana, acabado_aluminio, tipo_de_vidrio, esmerilado=False):
        self.ancho = ancho
        self.largo = largo
        self.estilo = estilo
        self.cantidad = cantidad
        self.estado_ventana = estado_ventana
        self.acabado_aluminio = acabado_aluminio
        self.tipo_de_vidrio = tipo_de_vidrio
        self.esmerilado = esmerilado

        self.validar_estilo()
        self.validar_acabado_aluminio()
        self.validar_tipo_vidrio()

    def validar_estilo(self):
        if self.estilo not in self.ESTILOS_VALIDOS:
            raise ValueError(f"Estilo de ventana '{self.estilo}' no es válido. Los estilos permitidos son: {', '.join(self.ESTILOS_VALIDOS)}")

    def validar_acabado_aluminio(self):
        if self.acabado_aluminio not in self.ACABADOS_ALUMINIO:
            raise ValueError(f"Acabado de aluminio '{self.acabado_aluminio}' no es válido. Los acabados permitidos son: {', '.join(self.ACABADOS_ALUMINIO)}")

    def validar_tipo_vidrio(self):
        if self.tipo_de_vidrio not in self.TIPOS_VIDRIO:
            raise ValueError(f"Tipo de vidrio '{self.tipo_de_vidrio}' no es válido. Los tipos permitidos son: {', '.join(self.TIPOS_VIDRIO)}")

    def calcular_costo(self):
        costo_aluminio = self.costo_aluminio()
        costo_vidrio = self.costo_vidrio()
        costo_esquinas = self.costo_esquinas()
        costo_chapas = self.costo_chapas()
        costo_total = costo_aluminio + costo_vidrio + costo_esquinas + costo_chapas

        if self.cantidad > 100:
            costo_total *= 0.9  # Aplicar descuento del 10%

        return costo_total

    def aplicar_descuento(self, descuento):
        return self.calcular_costo() * (1 - descuento / 100)

    def costo_esquinas(self):
        # Implementar lógica para calcular el costo de las esquinas
        return 10 * self.cantidad  # Ejemplo de costo fijo por esquina

    def costo_chapas(self):
        # Implementar lógica para calcular el costo de las chapas
        return 5 * self.cantidad  # Ejemplo de costo fijo por chapa

    def costo_vidrio(self):
        area_vidrio = (self.ancho - 0.03) * (self.largo - 0.03)
        costo_por_m2 = 50  # Ejemplo de costo por m²
        if self.esmerilado:
            costo_por_m2 += 10  # Costo adicional por esmerilado
        return area_vidrio * costo_por_m2 * self.cantidad

    def costo_aluminio(self):
        perimetro = 2 * (self.ancho + self.largo)
        costo_por_metro = 20  # Ejemplo de costo por metro
        return perimetro * costo_por_metro * self.cantidad