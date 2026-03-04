from metodos import Pizzeria

pizzeria = Pizzeria()

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("0.  mostrar menu")
    print("1. Buscar pizza por nombre")
    print("2. Mostrar inventario total")
    print("3. Mostrar pizza mas costosa")
    print("4. Salir")
    print("5. ordenar menu en ascendente")

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
        print("Saliendo del sistema...")
        break
    elif opcion == "5":
        matriz_ordenada = pizzeria.ordenar_ascendente()
        print("Menú ordenado en ascendente por precio:")

    else:
        print("Opción inválida")