from tkinter import*
app=Tk()
app.title("Aplicacion grafica en Python")
etiqueta=Label(app, text="Hola mundo!!!")
boton=Button(app, text="OK!!")
etiqueta.pack() #empaquetar y mostrar etiqueta en pantalla
boton.pack()#empaquetar y mostrar boton en pantalla
app.geometry("500x500")
app.mainloop()#cerrar el bucle principal
