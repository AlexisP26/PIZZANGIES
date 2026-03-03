from metodos import Pizzeria

pizzeria = Pizzeria()

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Buscar pizza por nombre")
    print("2. Mostrar inventario total")
    print("3. Mostrar pizza mas costosa")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
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
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")