def form():
    n1= int (input ("ingresa el valor hasta el que deseas llegar"))
    a=1
    sum=0

    while a<=n1:
        sum +=a**(a+1)
        a+=1

    res=sum/n1
    print(f"El resultado es:{res}")

def Dinero_a_gastar():
    saldo = float(input("Ingresa tu saldo disponible: "))

    while saldo > 0:
        producto = input("Ingresa el nombre del producto: ")
        costo = float(input(f"Ingrese el costo de {producto}: "))

        if costo > saldo:
            print("No tienes suficiente saldo.")
        else:
            saldo -= costo
            print(f"Has comprado {producto}. Saldo restante: {saldo}")

print("Tu saldo se ah agotado")


def generador_de_matriculas():
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
while True:
    print("MENU PRINCIPAL")
    print("1-FORMULA")
    print("2-DINERO A GASTAR")
    print("3-MATRICULA")
    opcion=int(input("Selecciona una opcion del MENU"))
    match opcion:
        case 1:
            form()
        case 2:
            Dinero_a_gastar()
        case 3:
            generador_de_matriculas()
        case _:
            print("operacion invalida")
    print("gracias por utilizar el programa")
    resp= input("\nDesea probar otra de las opciones del menu? (si/no):")
    if resp.lower() != "si":
        break
