class Ventana:
    def __init__(self, estilo, ancho, alto, acabado, tipo_vidrio, esmerilado=False):
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto
        self.acabado = acabado
        self.tipo_vidrio = tipo_vidrio
        self.esmerilado = esmerilado

    ancho = float(input("Ingrese el ancho de la ventana en (cm): "))
    alto = float(input("Ingrese el alto de la ventana en (cm): "))
    estilo = input("Ingrese el estilo de ventana que desea:\n -O \n -XO \n -OXXO \n -OXO \n =").upper()
    while estilo == "XOX":  
            print("Estilo de ventana no permitido")

    def calcular_costo():
        ancho = float(input("Ingrese el ancho de la ventana en (cm): "))
        alto = float(input("Ingrese el alto de la ventana en (cm): "))
        estilo = input("Ingrese el estilo de ventana que desea:\n -O \n -XO \n -OXXO \n -OXO \n =").upper()
        if estilo == "XOX":  
            print("Estilo de ventana no permitido")