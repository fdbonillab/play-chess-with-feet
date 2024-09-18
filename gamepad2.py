import pygame
import pyautogui
from pynput import mouse, keyboard
import tkinter as tk
from threading import Thread

ARRIBA = 0
ABAJO = 1
IZQUIERDA = 2
DERECHA = 3
ANCHO_CELDA = 94
ARRIBA_DERECHA = 6
listaPosiciones = []
# Crear referencias globales para las etiquetas de Tkinter
label_1 = None
label_2 = None
POSICION_INICIAL_CON_AUTOGUI = (2167, 190)
POSICION_FINAL_CON_AUTOGUI = (2737, 759)


# Iniciar el listener de teclado en un hilo separado
def start_keyboard_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Función para cerrar el programa cuando se presione la tecla Escape
def on_press(key):
    if key == keyboard.Key.esc:
        # Cerrar la ventana de Tkinter y detener el listener
        root.quit()  # Cerrar la ventana
        return False  # Salir del listener de teclado

# Función que se ejecuta cuando se detecta un clic
def on_click(x, y, button, pressed):
    if pressed:
        print(f"Clic detectado en ({x}, {y}) con el botón {button}")
        if not listaPosiciones:
            listaPosiciones.append((x, y))
        elif len(listaPosiciones) == 1:
            listaPosiciones.append((x, y))
        print(f"Lista de clics detectados {listaPosiciones}")
        actualizar_gui()

# Función para mover el ratón
def moverMouseA(x, y):
    print(f' lista posiciones size {len(listaPosiciones)}')

    if POSICION_INICIAL_CON_AUTOGUI:
        
        POSICION_INICIAL = None # = listaPosiciones[0]
        posicionFinal = None #= listaPosiciones[1]
        global ANCHO_CELDA
        #### se sobreescriben porque la posicion tomada con detecccion de click parece que no funciona bien a
        #### a 2 pantallas y seguramente si son de diferente resolucion

        POSICION_INICIAL = POSICION_INICIAL_CON_AUTOGUI 
        posicionFinal = POSICION_FINAL_CON_AUTOGUI
        
        
        print(f' posicion inicial {POSICION_INICIAL} ancho celda {ANCHO_CELDA} x: {x} y : {y} ')
        
        if POSICION_INICIAL[0] <= x <= posicionFinal[0] and POSICION_INICIAL[1] <= y <= posicionFinal[1]:
            # Mueve el ratón a las coordenadas (x, y)
            pyautogui.moveTo(x, y)
        else :
            ### el pad solo aplica si me tengo q mover a la casilla abajo a la derecha porque
            #### si ya estoy dentro del tablero el se movera segun donde haya dejado el puntero osea que tan agradable respecto
            ### de lo central depende de mi y no de la logica
            
            ANCHO_CELDA = (posicionFinal[0] - POSICION_INICIAL[0]) / 8
            pad = round(ANCHO_CELDA/2)
            print(f' pad {pad}')
            casillaAbajoDerecha = posicionFinal[0]-pad,posicionFinal[1]-pad
            print(f' posicion inicial {POSICION_INICIAL} , posicion final {POSICION_FINAL_CON_AUTOGUI} ancho celda {ANCHO_CELDA} x : {x} y : {y} casilla abajo derecha {casillaAbajoDerecha}')
            pyautogui.moveTo(casillaAbajoDerecha)

# Función para ejecutar el GUI de Tkinter
def start_tkinter_gui():
    global root
    global root, label_1, label_2  # Declarar las etiquetas como globales
    root = tk.Tk()
    root.title("Captura de clics")

    # Crear etiquetas para mostrar las coordenadas
    label_1 = tk.Label(root, text="Primer clic: No detectado")
    label_1.pack(pady=10)

    label_2 = tk.Label(root, text="Segundo clic: No detectado")
    label_2.pack(pady=10)

    root.mainloop()

# Función para actualizar la GUI de Tkinter desde los datos de `listaPosiciones`
def actualizar_gui():
    global label_1, label_2  # Usar las etiquetas globales
    if len(listaPosiciones) > 0:
        label_1.config(text=f"Primer clic para esquina superior izquierda : {listaPosiciones[0]}")
    if len(listaPosiciones) > 1:
        label_2.config(text=f"Segundo clic para esquina inferior derecha : {listaPosiciones[1]}")


# Crear un hilo para el listener del teclado
keyboard_thread = Thread(target=start_keyboard_listener)
keyboard_thread.start()

# Crear un hilo para el listener del ratón
mouse_thread = Thread(target=lambda: mouse.Listener(on_click=on_click).start())
mouse_thread.start()

# Crear un hilo para el GUI de Tkinter
tkinter_thread = Thread(target=start_tkinter_gui)
tkinter_thread.start()

# Inicializar pygame
pygame.init()

# Inicializar el joystick
pygame.joystick.init()

# Comprobar cuántos joysticks están conectados
joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print("No se detectó ningún joystick.")
else:
    # Seleccionar el primer joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print(f"Nombre del joystick: {joystick.get_name()}")
    print(f"Cantidad de ejes: {joystick.get_numaxes()}")
    print(f"Cantidad de botones: {joystick.get_numbuttons()}")

# Bucle principal de pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.JOYAXISMOTION:
            # Leer los ejes del joystick
            for i in range(joystick.get_numaxes()):
                axis_value = joystick.get_axis(i)
                print(f"Eje {i} valor: {axis_value}")

        if event.type == pygame.JOYBUTTONDOWN:
            # Imprime la posición actual del ratón
            x, y = pyautogui.position()
            # Leer los botones presionados
            for i in range(joystick.get_numbuttons()):
                button = joystick.get_button(i)
                if button:
                    #ANCHO_CELDA
                    print(f"Botón {i} presionado ancho celda aki {ANCHO_CELDA}")
                    if i == ARRIBA:
                        print("Moviendo arriba")
                        moverMouseA(x, y - ANCHO_CELDA)
                    if i == ABAJO:
                        print("Moviendo abajo")
                        moverMouseA(x, y + ANCHO_CELDA)
                    if i == IZQUIERDA:
                        print("Moviendo izquierda")
                        moverMouseA(x - ANCHO_CELDA, y)
                    if i == DERECHA:
                        print("Moviendo derecha")
                        moverMouseA(x + ANCHO_CELDA, y)
                    if i == ARRIBA_DERECHA:
                        pyautogui.click()

# Finalizar pygame
pygame.quit()
