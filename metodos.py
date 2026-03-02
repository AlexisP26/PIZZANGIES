from clase import Pizza
from clase import Pedido

class Pizzeria:
    def __init__(self):
        self.menu = [
            [
                Pizza("hawaiana", "pequeña", 10000),
                Pizza("hawaiana", "mediana", 15000),
                Pizza("hawaiana", "grande", 20000)
            ],
            [
                Pizza("pepperoni", "pequeña", 11000),
                Pizza("pepperoni", "mediana", 16000),
                Pizza("pepperoni", "grande", 21000)
            ],
            [
                Pizza("vegetariana", "pequeña", 12000),
                Pizza("vegetariana", "mediana", 17000),
                Pizza("vegetariana", "grande", 22000)
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