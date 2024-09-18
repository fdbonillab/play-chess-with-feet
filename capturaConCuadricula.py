import pyautogui
import cv2
import numpy as np
import time

# Espera 5 segundos para que tengas tiempo de mover el ratón a la posición deseada
time.sleep(5)

# Tomar una captura de pantalla
screenshot = pyautogui.screenshot()

# Convertir la imagen de PIL (formato de pyautogui) a un formato de OpenCV (numpy array)
screenshot = np.array(screenshot)

# Convertir la imagen de RGB (formato de pyautogui) a BGR (formato de OpenCV)
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

# Función para dibujar una matriz
def dibujar_matriz(imagen, start_point, filas, columnas, ancho_casilla, alto_casilla, color=(0, 255, 0), grosor=2):
    """Dibuja una matriz (grid) en la imagen.
    
    Args:
        imagen: La imagen donde se dibujará la matriz.
        start_point: (x, y) coordenadas de la esquina superior izquierda.
        filas: Número de filas en la matriz.
        columnas: Número de columnas en la matriz.
        ancho_casilla: Ancho de cada casilla.
        alto_casilla: Altura de cada casilla.
        color: Color de las líneas en formato BGR.
        grosor: Grosor de las líneas de la matriz.
    """
    x_start, y_start = start_point

    # Dibujar líneas horizontales
    for i in range(filas + 1):
        y = y_start + i * alto_casilla
        cv2.line(imagen, (x_start, y), (x_start + columnas * ancho_casilla, y), color, grosor)

    # Dibujar líneas verticales
    for j in range(columnas + 1):
        x = x_start + j * ancho_casilla
        cv2.line(imagen, (x, y_start), (x, y_start + filas * alto_casilla), color, grosor)

##  coordenda para tamamño de cuadriculas (381, 202) (475, 203) tons el ancho es 95
# Parámetros de la matriz
start_point = (381, 202)  # Esquina superior izquierda donde comenzará la matriz
filas = 8                 # Número de filas
columnas = 8              # Número de columnas
ancho_casilla = 94        # Ancho de cada casilla
alto_casilla = 94         # Altura de cada casilla
color = (0, 255, 0)       # Color de las líneas (verde)
grosor = 2                # Grosor de las líneas

# Dibujar la matriz en la captura de pantalla
dibujar_matriz(screenshot, start_point, filas, columnas, ancho_casilla, alto_casilla, color, grosor)

# Guardar la imagen con la matriz dibujada
cv2.imwrite('screenshot_with_grid.png', screenshot)

# Mostrar la imagen resultante en una ventana
cv2.imshow('Captura de pantalla con matriz', screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()
