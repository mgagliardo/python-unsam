class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def __repr__(self):
        return f"Lote de {self.cajones} cajones de {self.nombre}, pagados a ${self.precio} cada uno."

    def __str__(self):
        return f"Lote de {self.cajones} cajones de {self.nombre}, pagados a ${self.precio} cada uno."

    def costo(self):
        return self.cajones * self.precio

    def vender(self, cantidad):
        self.cajones -= cantidad
