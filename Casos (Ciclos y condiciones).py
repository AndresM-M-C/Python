a=int(input("Ingresa el primer numero"))
b=int(input("ingresa otro numero"))
print("MENU PRINCIPAL")
print ("{+} suma a+b")
print ("{-} resta a-b")
print ("{*} multiplica a*b")
print ("{/} divide a/b")
simbolo=input ("Ingresa una opcion ingresando el simbolo")
match simbolo:
    case "+":
        print ("El resultado", (a+b))
    case "-":    
        print ("El resultado", (a-b))
    case "*":    
        print ("El resultado", (a*b))
    case "/":
        if b !=0:
            print ("El resultado", a/b) 
        else: 
            print ("No se puede dividir entre cero") 
    case _:
        print ("Operacion invalida")     




