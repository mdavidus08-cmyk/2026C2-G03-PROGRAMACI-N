temperaturas = []
cantidad_registrada = 0

# Complete aquí el ciclo while.
while True:
    print("\n---- REGISTRO DE TEMPERATURAS ----")
    print("1. Registrar temperatura")
    print("2. Reporte temperaturas")
    print("3. Salir del sistema")

    opcion = input("Ingrese una opción del menu: ")

    if opcion == "1":
        temp = float(input("Ingrese la temperatura del día: "))
        temperaturas.append(temp)
        print("Registro agregado exitosamente! \n")
    elif opcion == "2":
        print("REPORTE TEMPERATURAS")
        cantidad = len(temperaturas)
        print(f"Cantidad temperaturas registradas: {cantidad}")
        print(f"Temperatura maxima: {max(temperaturas)}")
        print(f"Temperatura minima: {min(temperaturas)}")
        print(f"Temperatura promedio: {sum(temperaturas) / cantidad:.2f}")
    elif opcion == "3":
        print("Cerrando aplicación")
        break
    else:
        print("Opción invalida!!")
