def suma():
    x=int(input("dame un numero"))
    r=int(input("Dame otro numero"))
    z= x+r
    print("El resultado es--->", z)
    
def resta():
    x=int(input("dame un numero"))
    r=int(input("Dame otro numero"))
    z= x-r
    print("El resultado es--->", z)

def multiplicacion():
    x=int(input("dame un numero"))
    r=int(input("Dame otro numero"))
    z= x*r
    print("El resultado es--->", z)

def division():
    x=int(input("dame un numero"))
    r=int(input("Dame otro numero"))
    z= x/r
    print("El resultado es--->", z)

print("MENU PRINCIPAL")
print("{+} suma x+r")
print("{-} resta x-r")
print("{*} multiplica x*r")
print("{/} divide x/r")
simbolo=input("Selecciona la operacion a realizar ingresando un simbolo")
match simbolo:
    case"+":
        suma()
    case"-":
        resta()
    case"*":
        multiplicacion()
    case"/":
        division()
        
    case _:
        print("Operacion Invalida")        





    
        
    
        