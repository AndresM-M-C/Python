import tkinter as tk
from tkinter import ttk

def completar_barra():
    valor=barra_progreso['value']
    if valor <100:
        barra_progreso['value']= valor + 10
        actualizar_porcentaje()
        ventana.after(100, completar_barra)

def actualizar_porcentaje():
    valor=barra_progreso['value']
    porcentaje.set(f'{int(valor)}%')

ventana=tk.Tk()
ventana.title('barra de progreso')
ventana.geometry('300x300')
ventana.configure(bg="#CDD6DF")

#estilo para la barra de progreso y el boton
style= ttk.Style()
style.theme_use('clam')

#estilo para para la barra de progreso
style.configure(style="TProgressbar", troughcolor='#34495E',
background='#1ABC9C', thickness=50)
style.configure(style='TButton', font=('helvetica', 10, 'bold'),
background='#2980B9', foreground='white')
style.map(style='TButton', background=[('active', "#5A8CAD")])

barra_progreso= ttk.Progressbar(ventana, orient='horizontal', length=200,
                               mode='determinate', style="TProgressbar")
barra_progreso.pack(pady=40)

porcentaje=tk.StringVar()
porcentaje.set('0%')
etiqueta_porcentaje=tk.Label(ventana, textvariable=porcentaje,
                             font=('helvetica', 10, 'bold'),
                             
bg='#2C3E50', fg='white')
etiqueta_porcentaje.pack(pady=5)

boton_completar=ttk.Button(ventana, text='Guardar',
command=completar_barra, style="TButton")
boton_completar.pack(pady=9)

ventana.mainloop()