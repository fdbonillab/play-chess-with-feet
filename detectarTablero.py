import cv2
import numpy as np

# Capturar la pantalla (puedes usar bibliotecas como mss o PIL)
img = cv2.imread('pantallaChess_com.png')  # Imagen de ejemplo

# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar detección de bordes para encontrar el contorno del tablero
edges = cv2.Canny(gray, 50, 150)

# Encontrar contornos (posibles límites del tablero)
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos encontrados
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow('Contornos', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
