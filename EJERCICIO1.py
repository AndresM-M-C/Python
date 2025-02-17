# Función para solicitar una matriz de 3x3 al usuario
def ingresar_matriz(nombre):
    matriz = []
    print(f"\nIngresa los valores de la {nombre}:")
    for i in range(3):
        fila = []
        for j in range(3):
            valor = int(input(f"Fila {i+1}, Columna {j+1}: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

# Función para multiplicar en orden inverso
def multiplicar_matrices(matriz1, matriz2):
    resultado = [[0] * 3 for _ in range(3)]
    n = 2  # Índice para recorrer matriz2 en orden inverso
    for i in range(3):
        for j in range(3):
            resultado[i][j] = matriz1[i][j] * matriz2[n - i][n - j]
    return resultado

# Función para imprimir una matriz en formato de tabla
def imprimir_matriz(nombre, matriz):
    print(f"\n{name}:\n" + "-"*20)
    for fila in matriz:
        print(" | ".join(f"{num:3}" for num in fila))
    print("-"*20)

# Solicitar las matrices
matriz1 = ingresar_matriz("Matriz 1")
matriz2 = ingresar_matriz("Matriz 2")

# Multiplicar matrices
resultado = multiplicar_matrices(matriz1, matriz2)

# Imprimir matrices y resultado
imprimir_matriz("Matriz 1", matriz1)
imprimir_matriz("Matriz 2", matriz2)
imprimir_matriz("Matriz Resultado", resultado)
