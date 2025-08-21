import tkinter as tk
from tkinter import messagebox
raiz=tk.Tk() # la variable raiz toma el valor de modo grafico (ventana)
raiz.title("TECNOLOGICO DE ESTUDIOS SUPERIORES DE JILOTEPEC")
#raiz.resizable (Tue,True) # se puede ampliar con mouse tanto horizontal y vertical
raiz.geometry("700x400") #la ventana esta definida 700 HORIZONTAL por 400 VERTICAL
raiz.configure(bg="yellow")
def saludar():
    messagebox.askquestion("informacion", "programando en python")
button=tk.Button(raiz, text="click aqui", command=saludar)
button.pack()
raiz.mainloop ()

'''Tipos de mensajes
showwwarning,
showerror,
askquestion,
askokcancel,
askyesno,
askyesnocancel,
'''
    