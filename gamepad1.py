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
POSICION_INICIAL = (258, 192)

listaPosiciones = []

# Iniciar el listener de teclado en un hilo separado
def start_keyboard_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Función para cerrar el programa cuando se presione la tecla Escape
def on_press(key):
    if key == keyboard.Key.esc:
        # Cerrar la ventana de Tkinter y detener el listener
        root.quit()  # Cerrar la ventana
        #mouse_listener.stop()  # Detener el listener del ratón
        return False  # Salir del listener de teclado
# Función que se ejecuta cuando se detecta un clic
def on_click(x, y, button, pressed):
    if pressed:
        print(f"Clic detectado en ({x}, {y}) con el botón {button}")
        if not listaPosiciones:
            listaPosiciones.append((x,y))
        elif (len(listaPosiciones) == 1):
            listaPosiciones.append((x,y))
        print(f" lista clicks detectados {listaPosiciones}" )
def hacerClick():
     pyautogui.click()
def moverMouseA(x,y):
    '''
     (381, 202) y el ancho 94 quiere decir q 94 x 8 = 752 entonces 381 + 752 y 202 + 752  la coordenada de abajo a la derecha es 
     1133, 954
     entonces los limites son 381 <---> 1133 en x y 202 <----> 954 en y

    '''
    POSICION_INICIAL = listaPosiciones[0]
    posicionFinal = listaPosiciones[1]
    ANCHO_CELDA = (posicionFinal-POSICION_INICIAL)/8
    
    if x > POSICION_INICIAL[0] and POSICION_INICIAL[0] < POSICION_INICIAL[0]+(ANCHO_CELDA*8) :
        if y > POSICION_INICIAL[1] and y < POSICION_INICIAL[1]+(ANCHO_CELDA*8) :
            # Mueve el ratón a las coordenadas (x, y)
            pyautogui.moveTo(x,y)  # Cambia las coordenadas a las deseadas

    # Haz clic en esa posición
    #pyautogui.click()

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Captura de clics")

# Crear etiquetas para mostrar las coordenadas
label_1 = tk.Label(root, text="Primer clic: No detectado")
label_1.pack(pady=10)

label_2 = tk.Label(root, text="Segundo clic: No detectado")
label_2.pack(pady=10)

# Crear un hilo para el listener del teclado
keyboard_thread = Thread(target=start_keyboard_listener)
keyboard_thread.start()



# Iniciar el listener del ratón
with mouse.Listener(on_click=on_click) as listener:
    listener.join()



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

# Bucle principal
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
                    print(f"Botón {i} presionado")
                    if i == ARRIBA:# suponiendo q el boton 2 es hacia arriba
                       print(" moviendo arriba ")
                       moverMouseA(x,y-ANCHO_CELDA)
                    if i == ABAJO:# suponiendo q el boton 2 es hacia arriba
                       moverMouseA(x,y+ANCHO_CELDA)
                       print(" moviendo abajo ")
                    if i == IZQUIERDA:# suponiendo q el boton 2 es hacia arriba
                       moverMouseA(x-ANCHO_CELDA,y)
                       print(" moviendo izquierda ")
                    if i == DERECHA:# suponiendo q el boton 2 es hacia arriba
                       moverMouseA(x+ANCHO_CELDA,y)
                       print(" moviendo derecha ")
                    if i == ARRIBA_DERECHA:
                        hacerClick()

pygame.quit()
'''
                 0 arriba
 izquierda    2        3 derecha
                 1  abajo
'''