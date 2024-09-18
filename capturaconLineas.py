import pyautogui
import cv2
import numpy as np

# Tomar una captura de pantalla
screenshot = pyautogui.screenshot()

# Convertir la imagen de PIL (formato de pyautogui) a un formato de OpenCV (numpy array)
screenshot = np.array(screenshot)

# Convertir la imagen de RGB (formato de pyautogui) a BGR (formato de OpenCV)
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

# Dibujar una línea sobre la imagen
start_point = (100, 100)  # Punto de inicio (x, y)
end_point = (400, 400)    # Punto final (x, y)
color = (0, 0, 255)       # Color en formato BGR (rojo en este caso)
thickness = 5             # Grosor de la línea

cv2.line(screenshot, start_point, end_point, color, thickness)

# Guardar la imagen con la línea dibujada
cv2.imwrite('screenshot_with_line.png', screenshot)

# Mostrar la imagen resultante en una ventana   
cv2.imshow('Captura de pantalla con línea', screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()
