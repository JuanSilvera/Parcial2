Parcial = [[None for _ in range(6)] for _ in range(30)]
ingresadosMes = 0

while True:
    
    print("\n--- MENU DEL TALLER ---")
    print("1. Registrar ingreso de vehículo")
    print("2. Registrar salida de vehículo")
    print("3. Reporte de vehículos terminados")
    print("4. Reporte de todos los vehículos ingresados")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        if ingresadosMes < 30:
            placa = input("Placa del vehículo: ")
            nom = input("Nombre del propietario: ")
            cel = input("Número de celular: ")
            dia_ingreso = int(input("Día de ingreso (1-31): "))

            Parcial[ingresadosMes][0] = placa
            Parcial[ingresadosMes][1] = nom
            Parcial[ingresadosMes][2] = cel
            Parcial[ingresadosMes][3] = dia_ingreso
            Parcial[ingresadosMes][4] = None
            Parcial[ingresadosMes][5] = None

            ingresadosMes += 1
            print("Vehículo registrado exitosamente.")
       
        else:
            print("Límite mensual alcanzado (máximo 30 vehículos).")

    elif opcion == "2":
        placa_buscar = input("Ingrese la placa del vehículo a entregar: ")
        encontrado = False

        for i in range(ingresadosMes):
            if Parcial[i][0] == placa_buscar:
                encontrado = True
                dia_salida = int(input("Ingrese día de salida (1-31): "))
                Parcial[i][4] = dia_salida
                demora = dia_salida - Parcial[i][3]
                Parcial[i][5] = demora

                print(f"Salida registrada. El vehículo demoró {demora} días en reparación.")
                break

        if not encontrado:
            print("Placa no encontrada.")

    elif opcion == "3":
        print("\n--- Reporte de vehículos terminados ---")
        contador_terminados = 0

        for i in range(ingresadosMes):
            if Parcial[i][4] is not None:
                contador_terminados += 1
                print((f"Placa: {Parcial[i][0]} | Demora: {Parcial[i][5]} días"))
            print(f"Total de vehículos terminados: {contador_terminados}")

    elif opcion == "4":
        print("\n--- Reporte de todos los vehículos ingresados ---")
        for i in range(ingresadosMes):
            print(f"Placa: {Parcial[i][0]} | Propietario: {Parcial[i][1]} | Celular: {Parcial[i][2]} | Día de ingreso: {Parcial[i][3]} | Día de salida: {Parcial[i][4]} | Demora: {Parcial[i][5]} días")

    elif opcion == "5":
        print("Saliendo del programa.")
        break