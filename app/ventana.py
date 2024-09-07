class Ventana:
    ESTILOS_VALIDOS = ["O", "XO", "OXXO", "OXO"]
    ACABADOS_ALUMINIO = {
        "Pulido": 50700,
        "Lacado Brillante": 54200,
        "Lacado Mate": 53600,
        "Anodizado": 57300
    }
    TIPOS_VIDRIO = {
        "Transparente": 8.25,
        "Bronce": 9.15,
        "Azul": 12.75
    }
    COSTO_ESMERILADO = 5.20
    COSTO_ESQUINAS = 4310
    COSTO_CHAPAS = 16200

    def init(self, ancho, largo, estilo, cantidad, acabado_aluminio, tipo_de_vidrio, esmerilado=False):
        self.ancho = ancho
        self.largo = largo
        self.estilo = estilo
        self.cantidad = cantidad
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
            raise ValueError(f"Acabado de aluminio '{self.acabado_aluminio}' no es válido. Los acabados permitidos son: {', '.join(self.ACABADOS_ALUMINIO.keys())}")

    def validar_tipo_vidrio(self):
        if self.tipo_de_vidrio not in self.TIPOS_VIDRIO:
            raise ValueError(f"Tipo de vidrio '{self.tipo_de_vidrio}' no es válido. Los tipos permitidos son: {', '.join(self.TIPOS_VIDRIO.keys())}")

    def calcular_costo(self):
        costo_aluminio = self.costo_aluminio()
        costo_vidrio = self.costo_vidrio()
        costo_esquinas = self.costo_esquinas()
        costo_chapas = self.costo_chapas()
        costo_total = costo_aluminio + costo_vidrio + costo_esquinas + costo_chapas

        descuento_aplicado = False
        if self.cantidad > 100:
            costo_total *= 0.9  # Aplicar descuento del 10%
            descuento_aplicado = True

        return costo_total, descuento_aplicado

    def aplicar_descuento(self, descuento):
        return self.calcular_costo()[0] * (1 - descuento / 100)

    def costo_esquinas(self):
        return self.COSTO_ESQUINAS * 4 * self.cantidad

    def costo_chapas(self):
        if self.estilo != 'O' and 'X' in self.estilo:
            return self.COSTO_CHAPAS * self.cantidad
        return 0

    def costo_vidrio(self):
        area_vidrio = (self.ancho - 0.03) * (self.largo - 0.03)
        costo_por_cm2 = self.TIPOS_VIDRIO[self.tipo_de_vidrio]
        if self.esmerilado:
            costo_por_cm2 += self.COSTO_ESMERILADO
        return area_vidrio * costo_por_cm2 * self.cantidad

    def costo_aluminio(self):
        perimetro = 2 * (self.ancho + self.largo) - 8  # Descontar las esquinas
        costo_por_cm = self.ACABADOS_ALUMINIO[self.acabado_aluminio] / 100  # Convertir a costo por cm
        return perimetro * costo_por_cm * self.cantidad