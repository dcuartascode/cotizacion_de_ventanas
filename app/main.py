from naves import Naves
from ventana import Ventana

def ingresar_valores():
    ancho_nave = float(input("Ingrese el ancho de la nave: "))
    largo_nave = float(input("Ingrese el largo de la nave: "))

    ancho_ventana = float(input("Ingrese el ancho de la ventana: "))
    largo_ventana = float(input("Ingrese el largo de la ventana: "))
    estilo_ventana = input("Ingrese el estilo de la ventana (O, XO, OXXO, OXO): ").upper()
    cantidad_ventana = int(input("Ingrese la cantidad de ventanas: "))
    acabado_aluminio = input("Ingrese el acabado de aluminio (Pulido, Lacado Brillante, Lacado Mate, Anodizado): ")
    tipo_de_vidrio = input("Ingrese el tipo de vidrio (Transparente, Bronce, Azul): ")
    esmerilado = input("¿Desea agregar esmerilado al vidrio? (si/no): ").lower() == 'si'

    try:
        nave = Naves(ancho_nave, largo_nave)
        ventana = Ventana(ancho_ventana, largo_ventana, estilo_ventana, cantidad_ventana, acabado_aluminio, tipo_de_vidrio, esmerilado)

        print(f"Perímetro de la nave: {int(nave.perimetro())} m")
        print(f"Área de vidrio de la nave: {int(nave.area_vidrio())} m²")
        costo_total, descuento_aplicado = ventana.calcular_costo()
        print(f"Costo total de las ventanas: {costo_total}")
        if descuento_aplicado:
            print("Se aplicó un descuento del 10% por superar las 100 unidades.")
        else:
            print("No se aplicó descuento.")

        # Generar reporte de cotización
        generar_reporte(ventana, descuento_aplicado)

    except ValueError as e:
        print(e)

def generar_reporte(ventana, descuento_aplicado):
    reporte = f"""
    Reporte de Cotización:
    ----------------------
    Dimensiones de la ventana: {ventana.ancho} x {ventana.largo} m
    Estilo de la ventana: {ventana.estilo}
    Cantidad de ventanas: {ventana.cantidad}
    Acabado de aluminio: {ventana.acabado_aluminio}
    Tipo de vidrio: {ventana.tipo_de_vidrio}
    Esmerilado: {'Sí' if ventana.esmerilado else 'No'}
    Costo total: {ventana.calcular_costo()[0]}
    Descuento aplicado: {'Sí' if descuento_aplicado else 'No'}
    """
    print(reporte)

# Llamar a la función para ingresar valores
ingresar_valores()
