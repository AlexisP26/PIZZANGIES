class Pizza:
    def __init__ (self, nombre, tamaño, precio ):
        self.tipo = nombre
        self.tamaño = tamaño
        self.precio =precio 

class Pedido:
    def __init__ (self,pizza, cantidad ):
        self.pizza = pizza
        self.cantidad = cantidad
        self.total = pizza.precio*cantidad


