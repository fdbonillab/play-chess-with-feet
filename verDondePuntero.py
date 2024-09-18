import tkinter as tk
from PIL import ImageGrab, ImageTk
import pyautogui
import time

# Tamaño de la sección cuadrada que se mostrará
SECCION_SIZE = 200

def actualizar_imagen():
    # Obtener la posición del cursor
    x, y = pyautogui.position()
    
    # Calcular las coordenadas de la sección alrededor del cursor
    left = x - SECCION_SIZE // 2
    top = y - SECCION_SIZE // 2
    right = x + SECCION_SIZE // 2
    bottom = y + SECCION_SIZE // 2
    
    # Capturar la sección de la pantalla
    imagen = ImageGrab.grab(bbox=(left, top, right, bottom))
    
    # Convertir la imagen para usarla en Tkinter
    imagen = ImageTk.PhotoImage(imagen)
    
    # Actualizar el widget de imagen
    etiqueta_imagen.config(image=imagen)
    etiqueta_imagen.image = imagen
    
    # Actualizar cada 100 ms
    root.after(100, actualizar_imagen)

# Crear ventana Tkinter
root = tk.Tk()
root.title("Vista previa de pantalla alrededor del puntero")

# Etiqueta para mostrar la imagen
etiqueta_imagen = tk.Label(root)
etiqueta_imagen.pack()

# Iniciar la actualización de la imagen
actualizar_imagen()

# Iniciar el bucle de Tkinter
root.mainloop()
