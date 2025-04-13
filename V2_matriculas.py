import datetime
fecha = datetime.datetime.now()
año = fecha.strftime("%Y")

cont = 1

while True:
    print("\nCrear matrícula")
    
    print("Periodo:")
    print("1. Transferido de otra institucion")
    print("2. Admisión")
    periodo = int(input("Ingrese el periodo: "))

    while periodo != 1 and periodo != 2:
        print("Número de periodo inválido. Por favor, ingrese 1 o 2.")
        periodo = int(input("Ingrese el periodo: "))

    print("\nCarreras:")
    print("1. Ingeniería Industrial")
    print("2. TICS")
    print("3. Ingenieria en Sistemas Computacionales")
    print("4. Ingeniería Mecatronica")
    print("5. Ingeniería en Química")
    print("6. Ingeniería en Civil")
    print("7. Ingeniería en Logistica")
    print("8. Licenciatura en Administracion")
    carrera = int(input("Ingrese el número de carrera: "))

    while carrera < 1 or carrera > 8:
        print("Número de carrera inválido, ingrese un número entre 1 y 8.")
        carrera = int(input("Ingrese el número de carrera: "))

    if cont < 10:
        Secuencia = "00" + str(cont)
    elif cont < 100:
        Secuencia = "0" + str(cont)
    else:
        Secuencia = str(cont)

    matricula = f"{año}{periodo}{carrera}{Secuencia}"
    print(f"\nMatrícula creada: {matricula}")
    cont += 1

    respuesta = input("\n¿Desea crear otra matrícula? (s/n): ")
    if respuesta.lower() != "s":
        break
