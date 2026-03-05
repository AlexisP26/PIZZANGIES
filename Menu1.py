from metodos import Pizzeria

pizzeria = Pizzeria()

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("0.  mostrar menu")
    print("1. Buscar pizza por nombre")
    print("2. Mostrar inventario total")
    print("3. Mostrar pizza mas costosa")
    print("4. ordenar menu en ascendente")
    print("5. disponibilidad")
    print("6. agrupar por precio")
    print("7. agregar producto ")
    print("8. cantidad de productos en oferta ")
    print("9. vendedor con mas productos vendidos")

    print("10. Salir")
    
    opcion = input("Seleccione una opcion: ")

    if opcion == "0":
        pizzeria.mostrar_menu()
    elif opcion == "1":
        nombre = input("Ingrese nombre de la pizza: ")

        posicion = pizzeria.buscar_pizza_por_nombre(nombre)

        if posicion is not None:
            fila, columna = posicion
            print("La pizza está en:")
            print("Fila:", fila)
            print("Columna:", columna)
        else:
            print("Pizza no encontrada")

    elif opcion == "2":
        total = pizzeria.calcular_inventario_total()
        print("inventario total", total)

    elif opcion =="3":
        pizza = pizzeria.buscar_pizza_mas_costosa()
        if pizza is not None:
            print("Pizza más costosa:")
            print("Nombre:", pizza.nombre)
            print("Tamaño:", pizza.tamaño)
            print("Precio:", pizza.precio)
        
        else:
            print("pizza no encontrada")
        
    elif opcion == "4":
        matriz_ordenada = pizzeria.ordenar_ascendente()
        print("Menú ordenado en ascendente por precio:")
    
    elif opcion == "5":
        disponibles = pizzeria.Disponibilidad()

        if disponibles:
            for fila in disponibles:
                for pizza in fila:
                    print(pizza.nombre, pizza.tamaño, pizza.precio, pizza.cantidad,
                           pizza.oferta)
        else:
            print("No hay pizzas disponibles")
    
    elif opcion == "6":
        e, m, p = pizzeria.agrupar_por_precio()

        print("Económicas:")
        for pizza in e:
            print(pizza.nombre, pizza.precio)

        print("Medias:")
        for pizza in m:
            print(pizza.nombre, pizza.precio)

        print("Premium:")
        for pizza in p:
            print(pizza.nombre, pizza.precio)
        else:
            print("estas son las pizzas ordenadas por calidad")

    elif opcion == "7":
        pizzeria.agregar_producto()

    elif opcion == "8":
        productos_en_oferta = pizzeria.contar_productos_en_oferta()
        print("la cantidad de productos en oferta es", productos_en_oferta)
    
    elif opcion == "9":
        vendedor_del_mes , total_de_ventas = pizzeria.vendedor_con_mas_ventas(
            pizzeria.pedidos)
        print(vendedor_del_mes)
        print(total_de_ventas)
    
    elif opcion == "10":
        print("Saliendo del sistema...") 
        break