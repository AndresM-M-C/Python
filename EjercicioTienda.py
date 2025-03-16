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
