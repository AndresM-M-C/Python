import datetime
fecha=datetime.datetime.now()
año=datetime.datetime.strftime(fecha, "%Y")
numero=1

periodo=int(input("Ingresa el periodo en el que ingresaste entre las opciones 1 (El estudiante viene de otra institucion) y 2 (Admision al Tecnologico)"))
print("Ingresa el numero de carrera que Deseas Cursar")
print("MENU DE CARRERAS")
print("{1} ingenieria Industrial")
print("{2} TICS")
print("{3} ingenieria en sistemas computacionales")
print("{4} ingenieria Mecatronica")
print("{5} ingenieria Quimica")
print("{6} ingenieria Civil")
print("{7} ingenieria Logistica")
print("{8} licenciatura en Administracion")

simbolo=input ("Ingresa el numero de tu carrera")
match simbolo:
    case "1":
        print(1)
    case "2":
        print(2)
    case "3":
        print(3)
    case "4":
        print(4)
    case "5":
        print(5)
    case "6":
        print(6)
    case "7":
        print(7)
    case "8":
        print(8)                       
print(año,periodo,simbolo,numero)
numero +=1