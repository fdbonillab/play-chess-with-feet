import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Captura de clics")

# Crear etiquetas para mostrar las coordenadas
label_1 = tk.Label(root, text="Primer clic: No detectado")
label_1.pack(pady=10)

label_2 = tk.Label(root, text="Segundo clic: No detectado")
label_2.pack(pady=10)

# Variable para contar los clics
click_count = 0

# Función que se ejecuta cuando se hace clic en la ventana
def on_click(event):
    global click_count
    click_count += 1
    
    if click_count == 1:
        # Mostrar las coordenadas del primer clic
        label_1.config(text=f"Primer clic: ({event.x}, {event.y})")
    elif click_count == 2:
        # Mostrar las coordenadas del segundo clic
        label_2.config(text=f"Segundo clic: ({event.x}, {event.y})")
        # Deshabilitar el evento después de dos clics
        root.unbind("<Button-1>")

# Enlazar el evento de clic con la función `on_click`
root.bind("<Button-1>", on_click)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
