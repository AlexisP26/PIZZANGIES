from clase import Pizza
from clase import Pedido

class Pizzeria:
    def __init__(self):
        self.menu = [
            [
                Pizza("hawaiana1", "pequeña",40, 10000),
                Pizza("hawaiana2", "mediana",50, 12000),
                Pizza("hawaiana3", "grande",60, 15000)
            ]
        ]

        self.pedidos = []

    def buscar_pizza_por_nombre(self, nombre_buscado):
        for i in range(len(self.menu)):
            for j in range(len(self.menu[i])):
                pizza = self.menu[i][j]
                if pizza.tipo.lower() == nombre_buscado.lower():
                    return (i, j)
        return None
    

    def calcular_inventario_total(self):
        total = 0
        for i in range(len(Pizzeria.menu)):
            for j in range(len(Pizza.menu[i])):
                producto = Pizza.menu[i][j]
                if producto is not None:
                    total = total + producto.cantidad
                    return total 
    def buscar_pizza_mas_costosa(self):
        pizza_mas_costosa = None
        for i in range(len(self.menu)):
            for j in range(len(self.menu[i])):
                producto = self.menu[i][j]
                if producto is not None:
                    if pizza_mas_costosa is None or producto.precio > pizza_mas_costosa.precio:
                        pizza_mas_costosa = producto
        return pizza_mas_costosa