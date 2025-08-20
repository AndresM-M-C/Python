import tkinter as Tk #alias Tk

def suma():
    num1=int(entry_num1.get()) #entry_num1 es la caja de texto 1
    num2=int(entry_num2.get()) #entry_num2 es la caja de texto 1
    resultado=num1+num2
    label_resultado.config(text="resultado" + str(resultado)) #asigna el

app = Tk.Tk() #ventana o formulario= app el alias Tk
app.title("TECNOLOGICO DE ESTUDIOS SUPERIORES DE JILOTEPEC")

label_num1=Tk.Label(text="primer numero") #label_num1 es de tipo label
entry_num1=Tk.Entry() # capturar el primer valor

label_num2=Tk.Label(text="segundo numero")#label_num2 es de tipo label
entry_num2=Tk.Entry() #capturar el segundo valor

label_resultado = Tk.Label(text=" *****") #label resultado es de tipo
button_suma= Tk.Button(text="sumar", command=suma) #boton_suma es de tipo 

label_num1.pack() #empaquetar y mostrar label_num1 en pantalla
entry_num1.pack() #empaquetar y mostrar la caja de texto entry_num1 en pantalla
 
label_num2.pack()
entry_num2.pack()

label_resultado.pack()
button_suma.pack()

app.geometry("500x500")
app.mainloop()
