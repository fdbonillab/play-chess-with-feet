import pyautogui
import time

# Espera 5 segundos para que tengas tiempo de mover el ratón a la posición deseada
time.sleep(5)

# Imprime la posición actual del ratón
x, y = pyautogui.position()
print(f'Posición del ratón: ({x}, {y})')

# Mueve el ratón a las coordenadas (x, y)
pyautogui.moveTo(100, 200)  # Cambia las coordenadas a las deseadas

# Haz clic en esa posición
pyautogui.click()