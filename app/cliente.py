class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def obtener_info(self):
        return f"Nombre: {self.nombre}, Cédula: {self.cedula}, Teléfono: {self.telefono}"