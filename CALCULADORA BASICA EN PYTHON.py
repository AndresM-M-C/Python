import tkinter as tk

def agregar(valor):
    entrada.insert(tk.END, valor)

def borrar():
    texto = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, texto[:-1])

def limpiar():
    entrada.delete(0, tk.END)

def es_valida(expresion):
    caracteres_validos = "0123456789+-*/.() "
    return all(c in caracteres_validos for c in expresion)

def calcular():
    expresion = entrada.get()
    if es_valida(expresion):
        resultado = eval(expresion)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    else:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

ventana = tk.Tk()
ventana.title("CALCULADORA BASICA")
ventana.configure(bg="#bdccca")

entrada = tk.Entry(ventana, font=("Arial", 20), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('**', 4, 3),
    ('AC', 5, 0), ('Del', 5, 1), ('=', 5, 2)
]

for texto, fila, columna in botones:
    if texto == '=':
        boton = tk.Button(ventana, text=texto, width=11, height=2, font=("Arial", 14),
                          command=calcular)
        boton.grid(row=fila, column=columna, columnspan=2, padx=5, pady=5)
    elif texto == 'AC':
        boton = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 14),
                          command=limpiar)
        boton.grid(row=fila, column=columna, padx=5, pady=5)
    elif texto == 'Del':
        boton = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 14),
                          command=borrar)
        boton.grid(row=fila, column=columna, padx=5, pady=5)
    else:
        def crear_comando(v=texto):
            return lambda: agregar(v)
        boton = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 14),
                          command=crear_comando())
        boton.grid(row=fila, column=columna, padx=5, pady=5)

ventana.mainloop()
