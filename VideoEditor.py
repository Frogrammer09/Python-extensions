import pygame
from PIL import Image
import numpy as np
import cv2

modo=input("Quieres que se vea pixelado o con caracteres? P/C ")
while modo not in ["P","C"]:
    modo=input("Quieres que se vea pixelado o con caracteres? P/C ")
if modo == "C":
    text=input("Pon el caracter ")
    while len(text)!=1 or not text.isalpha():
        text=input("Error. Pon el caracter  ")
col=input("Quieres que sea a color? S/N ")
while col not in ["S","N"]:
    col=input("Error. Quieres que sea a color? S/N ")

camera = cv2.VideoCapture(0)


# Inicializar Pygame
pygame.init()
pygame.font.init()

# Definir el tamaño de la ventana
width = 400
height = 400
window_size = (width, height)
window = pygame.display.set_mode(window_size)

# Crear una superficie para dibujar
surface = pygame.Surface((48, 48))

# Bucle principal del juego
running = True
while running:

    window.fill((0, 0, 0))

    # Capturar una imagen
    ret, frame = camera.read()

    # Verificar si la captura fue exitosa
    if not ret:
        print("Error")

    # Cambiar la resolución
    resized_frame = cv2.resize(frame, (48, 48))

    resized_array = np.array(resized_frame)
    
    # Actualizar la ventana de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la superficie
    surface.fill((0, 0, 0))

    # Dibujar los cuadrados con los valores de r, g, b
    i=0
    row=0
    for rows in resized_array:
        pixel=0
        for pixels in rows:
            x = i % 48
            y = i // 48
            r=int(resized_array[row][pixel][0])
            g=int(resized_array[row][pixel][1])
            b=int(resized_array[row][pixel][2])
            font = pygame.font.Font(pygame.font.get_default_font(), 8)
            if col=="S":
                color=(b,g,r)
            else:
                color = ((r + g + b) // 3)
                color=(color,color,color)
            if modo == "P":
                pygame.draw.rect(surface, color, (x, y, 1, 1))
            else:
                text_surface = font.render(text, True, color)
                window.blit(text_surface, (x * 8, y * 8))
            i+=1
            pixel+=1
        row+=1
    # Actualizar la ventana
    if modo == "P":
        pygame.transform.scale(surface, window_size, window)
    pygame.display.update()


# Salir del programa
camera.release()
pygame.quit()







