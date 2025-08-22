import tkinter as tk  # Importamos la biblioteca tkinter para la interfaz gráfica
from tkinter import messagebox  # Importamos messagebox para mostrar ventanas emergentes
from gtts import gTTS  # Importamos gTTS para convertir texto a voz en formato .mp3
import os  # Biblioteca del sistema operativo, para borrar archivos
import threading  # Para ejecutar tareas en segundo plano sin congelar la ventana
import time  # Permite pausar la ejecución (sleep)
import uuid  # Genera identificadores únicos para evitar archivos repetidos
import pygame  # Biblioteca para reproducir audio sin errores en Windows

pygame.mixer.init()  # Inicializamos el reproductor de sonido de pygame

# Crear la ventana principal
root = tk.Tk()  # Inicializa la ventana
root.title("Juego del Gato")  # Título de la ventana
root.configure(bg="#d0f0c0")  # Fondo verde claro

# Variables globales
jugador_actual = ["A"]  # El jugador actual (usamos lista para poder modificar dentro de funciones)
simbolos = {"A": "X", "B": "O"}  # Diccionario de símbolos asignados a cada jugador
tablero = [""] * 9  # Lista que representa las 9 casillas del tablero
botones = []  # Lista que almacenará los botones del tablero

# Función para reproducir un texto como audio usando gTTS y pygame
def reproducir_audio(texto):
    def tarea():  # Esta función se ejecutará en un hilo separado
        try:
            time.sleep(1)  # Espera 1 segundo antes de reproducir el audio
            nombre_archivo = f"audio_{uuid.uuid4().hex}.mp3"  # Crea un nombre de archivo único
            tts = gTTS(text=texto, lang='es', slow=False)  # Convierte el texto a voz (rápido)
            tts.save(nombre_archivo)  # Guarda el archivo mp3
            pygame.mixer.music.load(nombre_archivo)  # Carga el archivo mp3
            pygame.mixer.music.play()  # Reproduce el archivo

            # Espera hasta que termine de reproducirse el audio
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
        except Exception as e:
            print("Error al reproducir audio:", e)  # Muestra error si ocurre algo
        finally:
            if os.path.exists(nombre_archivo):  # Si el archivo existe
                os.remove(nombre_archivo)  # Lo borra para limpiar archivos temporales

    threading.Thread(target=tarea).start()  # Inicia la reproducción en segundo plano

# Función para verificar si un jugador ganó
def verificar_ganador(simbolo):
    combinaciones = [  # Combinaciones ganadoras posibles
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
        (0, 4, 8), (2, 4, 6)              # Diagonales
    ]
    for a, b, c in combinaciones:  # Recorre cada combinación
        if tablero[a] == tablero[b] == tablero[c] == simbolo:  # Si hay 3 iguales
            return True  # Hay ganador
    return False  # Si no hay ganador

# Función para verificar si hay empate (todas las casillas llenas sin ganador)
def es_empate():
    return all(c != "" for c in tablero)  # Devuelve True si no hay espacios vacíos

# Función que se ejecuta al hacer clic en una casilla
def manejar_click(i):
    if tablero[i] == "":  # Si la casilla está vacía
        simbolo = simbolos[jugador_actual[0]]  # Obtiene el símbolo del jugador actual
        tablero[i] = simbolo  # Coloca el símbolo en la lista del tablero
        botones[i].config(text=simbolo, state="disabled", disabledforeground="black")  # Muestra símbolo en botón y lo desactiva

        if verificar_ganador(simbolo):  # Si el jugador ganó
            mensaje = f"¡Felicidades el Jugador {jugador_actual[0]} ha ganado!"  # Mensaje de victoria
            messagebox.showinfo("Fin del juego", mensaje)  # Muestra ventana emergente
            reproducir_audio(mensaje)  # Reproduce el mensaje por voz
            deshabilitar_todo()  # Desactiva todos los botones
        elif es_empate():  # Si hay empate
            mensaje = "¡Empate! No hay ganador."  # Mensaje de empate
            messagebox.showinfo("Empate", mensaje)  # Muestra mensaje
            reproducir_audio(mensaje)  # Reproduce el mensaje por voz
            deshabilitar_todo()  # Desactiva botones
        else:
            # Cambia al otro jugador
            jugador_actual[0] = "B" if jugador_actual[0] == "A" else "A"

# Desactiva todos los botones del tablero
def deshabilitar_todo():
    for boton in botones:
        boton.config(state="disabled")

# Reinicia el tablero y las variables para empezar de nuevo
def reiniciar_juego():
    for i in range(9):  # Recorre cada casilla
        tablero[i] = ""  # Borra el contenido
        botones[i].config(text="", state="normal", bg="#ffffff")  # Limpia el botón y lo reactiva
    jugador_actual[0] = "A"  # Reinicia el turno al jugador A

# Crea el marco (frame) donde van los botones del tablero
frame_tablero = tk.Frame(root, bg="#d0f0c0")
frame_tablero.pack(padx=10, pady=10)  # Muestra el frame con espacio alrededor

# Crea los 9 botones del tablero y los coloca en una cuadrícula 3x3
for i in range(9):
    btn = tk.Button(
        frame_tablero, text="", font=("Arial", 32), width=5, height=2,  # Estilo del botón
        bg="#ffffff", activebackground="#c0e0ff",  # Colores del botón
        command=lambda i=i: manejar_click(i)  # Asigna función al hacer clic
    )
    btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)  # Coloca el botón en la fila y columna correspondiente
    botones.append(btn)  # Agrega el botón a la lista

# Crea el botón para reiniciar el juego
btn_reiniciar = tk.Button(
    root, text="Reiniciar Juego", font=("Arial", 14, "bold"),
    bg="#ffcccb", command=reiniciar_juego  # Asigna función de reinicio
)
btn_reiniciar.pack(pady=10)  # Muestra el botón debajo del tablero

# Inicia el bucle principal de la ventana (mantiene la ventana abierta)
root.mainloop()
