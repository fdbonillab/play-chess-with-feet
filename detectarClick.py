from pynput import mouse

# Función que se ejecuta cuando se detecta un clic
def on_click(x, y, button, pressed):
    if pressed:
        print(f"Clic detectado en ({x}, {y}) con el botón {button}")

# Iniciar el listener del ratón
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
